import datetime
from datetime import datetime

from django.utils import timezone
import pytz
from random import randint, choice

from django.conf import settings
from django.http import Http404
from django.db import connection
from django.db.models import Case, ExpressionWrapper, DurationField, F, FloatField, OuterRef, Subquery, Value, When 
from django.db.models.aggregates import Count

from dispatch.models import Article, Page, Section, Subsection, Podcast, Image, ImageAttachment

from ubyssey.events.models import Event


class ArticleMixin(object):

    def __init__(self):
        pass

    def get_article(self, request, slug):
        """If the url requested includes the querystring parameters 'version' and 'preview_id',
        get the article with the specified version and preview_id.

        Otherwise, get the published version of the article.
        """
        return Article.objects.get(request=request, slug=slug, is_published=True)

    def get_reading_time(self, article):
        word_count = 0
        words_per_min = 150
        for block in article.content:
            if block['type'] == 'paragraph':
                word_count += len(block['data'].split(' '))

        reading_time = word_count // words_per_min
        return reading_time

    def insert_ads(self, content, article_type='desktop'):
        """Inject upto 5 ads evenly throughout the article content.
        Ads cannot inject directly beneath headers."""
        ad = {
            'type': 'ad',
            'data': article_type
        }

        paragraph_count = 1

        for block in content:
            paragraph_count = len([b for b in content if b['type'] == 'paragraph'])

        number_of_ads = 1
        paragraphs_per_ad = 6

        while paragraph_count / number_of_ads > paragraphs_per_ad :
            number_of_ads += 1
            if number_of_ads >= 5:
                paragraphs_per_ad = paragraph_count // number_of_ads
                break

        ad_count = 0
        paragraph_count = 0
        next_ad = randint(paragraphs_per_ad - 2, paragraphs_per_ad + 2)
        ad_placements = content

        for index, block in enumerate(content):
            if block['type'] == 'paragraph':
                paragraph_count += 1
            if paragraph_count == next_ad:
                    if index != 0 and content[index - 1]['type'] != 'header':
                        ad_placements.insert(index + ad_count, ad)
                        next_ad += randint(paragraphs_per_ad - 2, paragraphs_per_ad + 2)
                        ad_count += 1
                    else:
                        next_ad += 1

        return ad_placements

    def get_frontpage(self, sections=[], exclude=[], limit=7, is_published=True, max_days=14):

        reading_times = {
            'morning_start': '9:00:00',
            'midday_start': '11:00:00',
            'midday_end': '16:00:00',
            'evening_start': '16:00:00',
        }
        timeformat = '%H:%M:%S'
        articles = Article.objects.annotate(
            age = ExpressionWrapper(
                F('published_at') - timezone.now(),
                output_field=DurationField()
            ),
            reading = Case( 
                When(reading_time='morning', then=1.0 if timezone.now().time() < datetime.strptime(reading_times['morning_start'],timeformat).time() else 0.0),
                When(reading_time='midday', 
                    then=1.0 if (
                        timezone.now().time() >= datetime.strptime(reading_times['midday_start'],timeformat).time() and timezone.now().time() < datetime.strptime(reading_times['midday_start'],timeformat).time()
                    )  else 0.0),
                When(reading_time='evening', then=1.0 if timezone.now().time() <= datetime.strptime(reading_times['evening_start'],timeformat).time() else 0.0),
                default = Value(0.5),
                output_field=FloatField()
            ),
        ).filter(
            head=1,
            is_published=is_published,
            section__slug__in=sections # See this link for why you can do this instead of SQL joining: https://docs.djangoproject.com/en/3.0/topics/db/queries/#lookups-that-span-relationships
        ).exclude(
            parent_id__in=exclude
        ).order_by(
            '-published_at'
        )[:limit]
        
        return list(articles)

    def get_frontpage_sections(self, exclude=None):

        exclude = exclude or []
        results = {}

        sections = Section.objects.all()

        for section in sections:
            articles = Article.objects.exclude(id__in=exclude).filter(section=section,is_published=True).order_by('-published_at').select_related()[:5]
            if len(articles):
                results[section.slug] = {
                    'first': articles[0],
                    'stacked': articles[1:3],
                    'bullets': articles[3:],
                    'rest': articles[1:4],
                }

        return results

    def get_reading_list(self, article, ref=None, dur=None):
        articles = []
        name = None
        if ref is not None:
            if ref == 'frontpage':
                articles = self.get_frontpage(exclude=[article.parent_id])
                name = 'Top Stories'
            elif ref == 'popular':
                articles = self.get_popular(dur=dur).exclude(pk=article.id)[:5]
                name = "Most popular this week"
        else:
            articles = article.get_related()
            name = article.section.name

        return {
            'ids': ",".join([str(a.parent_id) for a in articles]),
            'name': name
        }

    def get_years(self):
        publish_dates = Article.objects.filter(is_published=True).dates('published_at','year',order='DESC')
        years = []

        for publish_date in publish_dates:
            years.append(publish_date.year)

        return years

    def get_topic(self, topic_name):

        return Article.objects.filter(
            is_published=True,
            topic__name=topic_name
        )

    def is_explicit(self, article):
        explicit_tags = ['sex', 'explicit']
        tags = article.tags.all().values_list('name', flat=True)
        for tag in tags:
            if tag.lower() in explicit_tags:
                return True
        return False

    def get_random_articles(self, n, section, exclude=None):
        """Returns `n` random articles from the given section."""

        # Get all articles in section
        queryset = Article.objects.filter(is_published=True, section__slug=section)

        # Exclude article (optional)
        if exclude:
            queryset = queryset.exclude(id=exclude)

        # Get article count
        count = queryset.aggregate(count=Count('id'))['count']

        # Get all articles
        articles = queryset.all()

        # Force a query (to optimize later calls to articles[index])
        list(articles)

        results = []
        indices = set()

        # n is bounded by number of articles in database
        n = min(count, n)

        while len(indices) < n:
            index = randint(0, count - 1)

            # Prevent duplicate articles
            if index not in indices:
                indices.add(index)
                results.append(articles[index])

        return results

    def get_popular(self, dur='week'):
        """Returns the most popular articles in the time period."""

        durations = {
            'week': 7,
            'month': 30
        }

        articles = Article.objects.filter(is_published=True)

        if dur in durations:
            end = timezone.now() + timezone.timedelta(days=1)
            start = end - timezone.timedelta(days=durations[dur])
            time_range = (start, end)
            articles = articles.filter(created_at__range=(time_range))

        return articles.order_by('-views')

    def get_suggested(self, article):
        """Returns the suggested articles for a current article"""
        subsection = article.get_subsection()

        if subsection:
            return subsection.get_published_articles().exclude(id=article.id)

        return Article.objects.filter(is_published=True).order_by('-published_at').exclude(id=article.id)
        
    def get_breaking_news(self):
        """Returns breaking news stories"""
        return Article.objects.filter(is_published=True, is_breaking=True, breaking_timeout__gte=timezone.now())

    def get_trending(self):
        """Returns the most trending articles in the time period."""

        DURATION = 6

        articles = Article.objects.filter(is_published=True)

        end = timezone.now()
        start = end - timezone.timedelta(hours=DURATION)
        time_range = (start, end)
        trending_articles = articles.filter(
            published_at__range=(time_range),
            views__gt=1000)

        if len(trending_articles) == 0:
            trending_article = None
        else:
            trending_article = choice(trending_articles)

        return trending_article

    def get_meta(self, article, default_image=None):
        try:
            image = article.featured_image.image.get_medium_url()
        except:
            image = default_image

        return {
            'title': article.headline,
            'description': article.seo_description if article.seo_description is not None else article.snippet,
            'url': article.get_absolute_url,
            'image': image,
            'author': article.get_author_type_string()
        }

# Generated by Django 3.2.11 on 2023-03-08 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_articlepage_use_parent_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='noindex',
            field=models.BooleanField(default=False, help_text='Warning: Only to be used when an article is requested to be unpublished, as per unpublishing policy. Should be FALSE in all but exceptional circumstances!', verbose_name="Add 'noindex' tag?"),
        ),
    ]
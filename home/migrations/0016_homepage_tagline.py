# Generated by Django 3.2.11 on 2023-06-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_homepage_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='tagline',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

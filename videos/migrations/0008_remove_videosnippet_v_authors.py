# Generated by Django 3.2.5 on 2022-02-23 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_videosnippet_v_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videosnippet',
            name='v_authors',
        ),
    ]

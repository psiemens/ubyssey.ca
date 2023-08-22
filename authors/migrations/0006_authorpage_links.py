# Generated by Django 3.2.11 on 2023-05-17 03:58

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0005_alter_authorpage_ubyssey_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorpage',
            name='links',
            field=wagtail.core.fields.StreamField([('url', wagtail.core.blocks.URLBlock(label='Url'))], blank=True),
        ),
    ]

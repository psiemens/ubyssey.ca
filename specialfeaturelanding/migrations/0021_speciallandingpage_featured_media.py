# Generated by Django 3.2.11 on 2023-08-25 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_ubysseyimage_legacy_pk'),
        ('specialfeaturelanding', '0020_speciallandingpage_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciallandingpage',
            name='featured_media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.ubysseyimage'),
        ),
    ]
# Generated by Django 3.2.5 on 2021-11-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_authorpage_legacy_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorpage',
            name='ubyssey_role',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Role at The Ubyssey'),
        ),
    ]

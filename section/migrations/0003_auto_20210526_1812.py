# Generated by Django 3.1.8 on 2021-05-27 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_auto_20210526_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsectionsorderable',
            name='subsection_snippet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='section.subsectionsnippet'),
        ),
    ]

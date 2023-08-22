# Generated by Django 3.2.11 on 2023-06-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0005_alter_authorpage_ubyssey_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authorpage',
            old_name='description',
            new_name='bio_description',
        ),
        migrations.AddField(
            model_name='authorpage',
            name='short_bio_descriptionn',
            field=models.TextField(blank=True, default=''),
        ),
    ]

# Generated by Django 3.1.12 on 2021-07-05 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0003_auto_20210705_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorysnippet',
            old_name='name',
            new_name='title',
        ),
    ]

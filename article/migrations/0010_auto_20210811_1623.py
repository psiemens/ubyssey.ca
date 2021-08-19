# Generated by Django 3.2.5 on 2021-08-11 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20210810_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='fw_about_this_article',
            field=models.TextField(blank=True, default='', verbose_name='About This Article (Optional)'),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='header_layout',
            field=models.CharField(default='right-image', help_text='Legacy from Dispatch\'s "Templates" feature', max_length=50),
        ),
    ]
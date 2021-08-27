# Generated by Django 3.2.5 on 2021-08-27 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_adsettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adslot',
            options={'ordering': ['id']},
        ),
        migrations.AddIndex(
            model_name='adslot',
            index=models.Index(fields=['slug'], name='ads_adslot_slug_05f149_idx'),
        ),
    ]

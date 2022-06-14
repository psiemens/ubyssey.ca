# Generated by Django 3.2.11 on 2022-06-09 21:59

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('ads', '0007_auto_20210904_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdTagSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdPlacementOrderable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('ad_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ads.adslot', verbose_name='Ad Slot')),
                ('settings', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_placement_orderables', to='ads.adtagsettings')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdHeadOrderable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('ad_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ads.adslot', verbose_name='Ad Slot')),
                ('settings', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_head_orderables', to='ads.adtagsettings')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]

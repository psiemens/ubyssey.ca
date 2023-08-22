# Generated by Django 3.2.11 on 2022-09-17 05:35

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('specialfeaturelanding', '0015_speciallandingpage_use_parent_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciallandingpage',
            name='editorial_stream',
            field=wagtail.core.fields.StreamField([('banner', wagtail.core.blocks.StructBlock([('template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Wagtail default'), ('guide-2021-banner.html', 'guide-2021-banner.html')], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title1', wagtail.core.blocks.CharBlock()), ('title2', wagtail.core.blocks.CharBlock()), ('credit', wagtail.core.blocks.CharBlock())])), ('credits', wagtail.core.blocks.StructBlock([('template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Wagtail default'), ('guide-2021-editorial-stream.html', 'guide-2021-editorial-stream.html')], required=False)), ('stream', wagtail.core.blocks.StreamBlock([('raw_html', wagtail.core.blocks.RawHTMLBlock()), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('editor_credit', wagtail.core.blocks.StructBlock([('template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Wagtail default'), ('guide-2021-editor-credit.html', 'guide-2021-editor-credit.html')], required=False)), ('role', wagtail.core.blocks.CharBlock()), ('name', wagtail.core.blocks.CharBlock())]))]))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('note_with_header', wagtail.core.blocks.StructBlock([('template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Wagtail default'), ('guide-2021-editors-note.html', 'guide-2021-editors-note.html'), ('guide-2021-land-acknowledgement.html', 'guide-2021-land-acknowledgement.html')], required=False)), ('title', wagtail.core.blocks.CharBlock()), ('rich_text', wagtail.core.blocks.RichTextBlock())])), ('graphical_menu', wagtail.core.blocks.StructBlock([('template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Wagtail default'), ('guide-2021-graphical-menu.html', 'guide-2021-graphical-menu.html')], required=False)), ('stream', wagtail.core.blocks.StreamBlock([('raw_html', wagtail.core.blocks.RawHTMLBlock()), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('graphical_menu_item', wagtail.core.blocks.StructBlock([('template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Wagtail default'), ('guide-2021-graphical-menu-item.html', 'guide-2021-graphical-menu-item.html')], required=False)), ('div_class_name', wagtail.core.blocks.CharBlock(default='box', max_length=255, required=True)), ('img_class_name', wagtail.core.blocks.CharBlock(default='photo_cover', max_length=255, required=True)), ('link', wagtail.core.blocks.URLBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('width', wagtail.core.blocks.IntegerBlock(required=False)), ('height', wagtail.core.blocks.IntegerBlock(required=False))]))]))])), ('child_articles', wagtail.core.blocks.StructBlock([])), ('flex_stream', wagtail.core.blocks.StructBlock([('template', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Wagtail default'), ('2022-div-stream-block.html', '2022-div-stream-block.html')], required=False)), ('class_selector', wagtail.core.blocks.CharBlock()), ('stream', wagtail.core.blocks.StreamBlock([('raw_html', wagtail.core.blocks.RawHTMLBlock()), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))]))], blank=True, null=True),
        ),
    ]

from wagtail.core import blocks
from wagtail.core.blocks import field_block
from images import blocks as image_blocks
from videos import blocks as video_blocks
from wagtail.documents.blocks import DocumentChooserBlock

class PullQuoteBlock(blocks.StructBlock):
    content = blocks.CharBlock(required=True)
    source =  blocks.CharBlock(required=False)
    audio = DocumentChooserBlock(required=False, help_text="optional, must be mp3 format")

    class Meta:
        template = 'article/stream_blocks/quote.html',
        icon = "openquote"

class ChooseSideBlock(blocks.ChoiceBlock):
    choices=[('left', 'Left'),('right', 'Right'),]
    required=True

class ChooseViewBlock(blocks.StructBlock):
    view = blocks.ChoiceBlock(
        choices=[('vs-side-by-side', 'Side By Side'),('vs-over-image', 'Text Over Image'),],
        default=('vs-over-image', 'Text Over Image'),
        required=True
    )

    class Meta:
        template = "article/stream_blocks/ve_switch_view.html",
        icon = "view"

class GapBlock(blocks.StructBlock):
    id = blocks.CharBlock(required=False)
    height = blocks.IntegerBlock(required=True, default=0, min_value=0)

    class Meta:
        template = 'article/stream_blocks/ve_gap.html',
        icon = "arrows-up-down"

class VisualEssayBlock(blocks.StructBlock):
    view = ChooseViewBlock()
    content = blocks.StreamBlock([
        ('rich_text', blocks.StructBlock(
            [
                ('block', blocks.RichTextBlock(                                
                    label="Rich Text Block",
                    help_text = "Write your article contents here. See documentation: https://docs.wagtail.io/en/latest/editor_manual/new_pages/creating_body_content.html#rich-text-fields"
                )),
                ('side',ChooseSideBlock(default=("right", "Right"))),
            ], icon = "doc-full"
        )),
        ('image', blocks.StructBlock(
            [
                ('block', image_blocks.ImageBlock()),
                ('side',ChooseSideBlock(default=("left", "Left"))),
            ], icon = "image"
        )),
        ('video', blocks.StructBlock(
            [
                ('block', video_blocks.OneOffVideoBlock(
                    label = "Credited/Captioned One-Off Video",
                    help_text = "Use this to credit or caption videos that will only be associated with this current article, rather than entered into our video library. You can also embed videos in a Rich Text Block."
                )),
                ('side',ChooseSideBlock(default=("left", "Left"))),
            ], icon = "media"
        )),
        ('raw_html', blocks.StructBlock(
            [
                ('block', blocks.RawHTMLBlock(
                    label = "Raw HTML Block",
                    help_text = "WARNING: DO NOT use this unless you really know what you're doing!"
                )),
                ('side',ChooseSideBlock(default=("left", "Left"))),
            ], icon = "code"
        )),
        ('quote', blocks.StructBlock(
            [
                ('block', PullQuoteBlock()),
                ('side',ChooseSideBlock(default=("left", "Left"))),
            ], icon = "openquote"
        )),
        ('gap', GapBlock()),
        ('switch_view', ChooseViewBlock()),
    ])

    class Meta:
        template = 'article/stream_blocks/visual-essay.html',
        icon = "form"

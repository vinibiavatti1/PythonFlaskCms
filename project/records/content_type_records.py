"""
Content records module.
"""
from project.models.content_type_model import ContentTypeModel
from project.properties.contents.article_properties import article_properties
from project.properties.contents.landing_properties import landing_properties
from project.properties.contents.event_properties import event_properties
from project.properties.contents.news_properties import news_properties
from project.properties.contents.post_properties import post_properties
from project.properties.contents.custom_properties import custom_properties


content_type_records: list[ContentTypeModel] = [
    ContentTypeModel(
        label='Article',
        name='article',
        template='article.html',
        icon='bi-files',
        properties=article_properties,
        allow_blocks=True,
    ),
    ContentTypeModel(
        label='Landing',
        name='landing',
        template='landing.html',
        icon='bi-layers',
        properties=landing_properties,
        allow_blocks=True,
    ),
    ContentTypeModel(
        label='Event',
        name='event',
        template='event.html',
        icon='bi-calendar-event',
        properties=event_properties,
        allow_blocks=True,
    ),
    ContentTypeModel(
        label='News',
        name='news',
        template='news.html',
        icon='bi-newspaper',
        properties=news_properties,
        allow_blocks=True,
    ),
    ContentTypeModel(
        label='Post',
        name='post',
        template='post.html',
        icon='bi-pin-angle',
        properties=post_properties,
        allow_blocks=True,
    ),
    ContentTypeModel(
        label='Custom',
        name='custom',
        template='custom.html',
        icon='bi-filetype-html',
        properties=custom_properties,
        allow_blocks=True,
    ),
    # Add more...
]

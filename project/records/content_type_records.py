"""
Content type records module.
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
        name='article',
        template='article.html',
        properties=article_properties,
        allow_blocks=True,
    ),
    ContentTypeModel(
        name='landing',
        template='landing.html',
        properties=landing_properties,
        allow_blocks=True,
    ),
    ContentTypeModel(
        name='event',
        template='event.html',
        properties=event_properties,
        allow_blocks=True,
    ),
    ContentTypeModel(
        name='news',
        template='news.html',
        properties=news_properties,
        allow_blocks=True,
    ),
    ContentTypeModel(
        name='post',
        template='post.html',
        properties=post_properties,
        allow_blocks=True,
    ),
    ContentTypeModel(
        name='custom',
        template='custom.html',
        properties=custom_properties,
        allow_blocks=True,
    ),
    # Add more.
]

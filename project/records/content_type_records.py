"""
Content records module.
"""
from project.models.record_type_model import RecordTypeModel
from project.properties.contents.article_properties import article_properties
from project.properties.contents.landing_properties import landing_properties
from project.properties.contents.event_properties import event_properties
from project.properties.contents.news_properties import news_properties
from project.properties.contents.post_properties import post_properties
from project.properties.contents.custom_properties import custom_properties
from project.enums import nested_object_type_enum
from project.enums import object_subtype_enum


content_type_records: list[RecordTypeModel] = [
    RecordTypeModel(
        label='Article',
        name=object_subtype_enum.ARTICLE_CONTENT,
        template='article.html',
        icon='bi-files',
        properties=article_properties,
        nested_objects=[nested_object_type_enum.BLOCK],
    ),
    RecordTypeModel(
        label='Landing',
        name=object_subtype_enum.LANDING_CONTENT,
        template='landing.html',
        icon='bi-layers',
        properties=landing_properties,
        nested_objects=[nested_object_type_enum.BLOCK],
    ),
    RecordTypeModel(
        label='Event',
        name=object_subtype_enum.EVENT_CONTENT,
        template='event.html',
        icon='bi-calendar-event',
        properties=event_properties,
        nested_objects=[nested_object_type_enum.BLOCK],
    ),
    RecordTypeModel(
        label='News',
        name=object_subtype_enum.NEWS_CONTENT,
        template='news.html',
        icon='bi-newspaper',
        properties=news_properties,
        nested_objects=[nested_object_type_enum.BLOCK],
    ),
    RecordTypeModel(
        label='Post',
        name=object_subtype_enum.POST_CONTENT,
        template='post.html',
        icon='bi-pin-angle',
        properties=post_properties,
        nested_objects=[nested_object_type_enum.BLOCK],
    ),
    RecordTypeModel(
        label='Custom',
        name=object_subtype_enum.CUSTOM_CONTENT,
        template='custom.html',
        icon='bi-filetype-html',
        properties=custom_properties,
        nested_objects=[nested_object_type_enum.BLOCK],
    ),
    # Add more...
]

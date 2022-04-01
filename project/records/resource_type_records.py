"""
Resource records module.
"""
from project.models.resource_type_model import ResourceTypeModel
from project.properties.contents.article_properties import article_properties
from project.properties.contents.landing_properties import landing_properties
from project.properties.contents.event_properties import event_properties
from project.properties.contents.news_properties import news_properties
from project.properties.contents.post_properties import post_properties
from project.properties.contents.custom_properties import custom_properties


resource_type_records: list[ResourceTypeModel] = [
    ResourceTypeModel(
        name='translations',
        icon='bi-translate',
        properties=article_properties,
    ),
    ResourceTypeModel(
        name='landing',
        icon='bi-layers',
        properties=landing_properties,
    ),
    ResourceTypeModel(
        name='event',
        icon='bi-calendar-event',
        properties=event_properties,
    ),
    # Add more...
]

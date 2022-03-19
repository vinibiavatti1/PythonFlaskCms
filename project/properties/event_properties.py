"""
Event properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.properties.extensions.seo_properties import seo_properties
from project.properties.extensions.sitemap_properties import sitemap_properties
from project.properties.extensions.content_properties import content_properties
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union


# Properties
event_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Event',
    ),
    PropertyModel(
        name='event_name',
        label='Event name',
        property_type=prop_type.STR,
        description='The name of the event',
        placeholder='Enter the event name',
        required=True,
    ),
    PropertyModel(
        name='event_description',
        label='Event description',
        property_type=prop_type.TEXT,
        description='The description of the event',
        placeholder='Enter the event description',
        required=True,
    ),
    PropertyModel(
        name='event_begin_date',
        label='Begin date',
        property_type=prop_type.DATETIME,
        description='Enter the begin date',
    ),
    PropertyModel(
        name='event_end_date',
        label='End date',
        property_type=prop_type.DATETIME,
        description='Enter the end date',
    ),
    PropertyModel(
        name='event_show_in_calendar',
        label='Show in calendar',
        property_type=prop_type.BOOL,
        description='Set to True to show the event in the calendar page',
        default=str_type.TRUE,
        required=True,
    ),
]

# Extensions
event_properties.extend(content_properties)
event_properties.extend(seo_properties)
event_properties.extend(sitemap_properties)

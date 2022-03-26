"""
List properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union


list_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='List'
    ),
    PropertyModel(
        label='Title',
        name='list_title',
        property_type=prop_type.STR,
        description='Title of the content that will be shown in list cards.',
        required=True,
    ),
    PropertyModel(
        label='Summary',
        name='list_summary',
        property_type=prop_type.TEXT,
        description='Summary of the content that will be shown in list cards.',
    ),
    PropertyModel(
        label='Thumbnail',
        name='list_thumbnail',
        property_type=prop_type.IMAGE,
        description='Thumbnail of the content that will be shown in list '
                    'cards.',
    ),
    PropertyModel(
        label='Thumbnail Description',
        name='list_thumbnail_alt',
        property_type=prop_type.TEXT,
        description='Thumbnail description (alt text)',
    ),
    PropertyModel(
        label='Show in lists?',
        name='list_show',
        property_type=prop_type.BOOL,
        description='Set to True to show this content in the list pages.',
        default=str_type.TRUE,
        required=True,
    ),
]

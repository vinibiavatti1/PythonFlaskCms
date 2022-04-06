"""
Announcement properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union
from project.properties.bases.resource_properties import resource_properties

# Properties
announcement_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Announcement'
    ),
    PropertyModel(
        name='announcement_link',
        label='Link',
        property_type=prop_type.URL,
        description='Announcement link',
        placeholder='Enter the announcement link',
    ),
    PropertyModel(
        name='announcement_container',
        label='Container',
        property_type=prop_type.ENUM,
        description='Announcement exibition container',
        enum_values=dict(
            all='All',
            vertical='Vertical Rectangle',
            horizontal='Horizontal Rectangle',
        ),
        default='all',
    ),
    PropertyModel(
        name='announcement_begin_date',
        label='Begin date',
        property_type=prop_type.DATETIME,
        description='Date to activate this announcement in website',
        placeholder='Enter the activation date',
    ),
    PropertyModel(
        name='announcement_end_date',
        label='End date',
        property_type=prop_type.DATETIME,
        description='Date to expire this announcement in website',
        placeholder='Enter the expiration date',
    ),
]

# Extensions
announcement_properties.extend(resource_properties)

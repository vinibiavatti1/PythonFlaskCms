"""
Sitemap properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union


sitemap_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Sitemap'
    ),
    PropertyModel(
        label='Show in sitemap',
        name='sitemap_active',
        property_type=prop_type.BOOL,
        description='Show this resource in sitemap',
        default=str_type.TRUE,
        required=True,
    ),
    PropertyModel(
        label='Priority',
        name='sitemap_priority',
        property_type=prop_type.ENUM,
        enum_values={
            '0.0': '0.0',
            '0.1': '0.1',
            '0.2': '0.2',
            '0.3': '0.3',
            '0.4': '0.4',
            '0.5': '0.5',
            '0.6': '0.6',
            '0.7': '0.7',
            '0.8': '0.8',
            '0.9': '0.9',
            '1.0': '1.0',
        },
        description='Set the priority 0.0 ~ 1.0 in sitemap',
        default='0.5',
        required=True,
    ),
    PropertyModel(
        label='Change frequently',
        name='sitemap_change_frequently',
        property_type=prop_type.ENUM,
        description='Set the change frequently to sitemap',
        enum_values={
            'always': 'always',
            'hourly': 'hourly',
            'daily': 'daily',
            'weekly': 'weekly',
            'monthly': 'monthly',
            'yearly': 'yearly',
            'never': 'never',
        },
        default='always',
        required=True,
    ),
]

"""
Redirects properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union
from project.properties.extensions.content_properties import content_properties


# Properties
redirect_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Redirect'
    ),
    PropertyModel(
        label='Target Type',
        name='target_type',
        property_type=prop_type.ENUM,
        enum_values={
            'url': 'URL',
            'regex': 'Regular Expression Pattern',
        },
        default='url',
        description='Type of the target (Regular Expression or URL).',
        required=True,
    ),
    PropertyModel(
        label='Target',
        name='target',
        placeholder='Enter the target pattern/address',
        property_type=prop_type.STR,
        description='Pattern or address to activate the redirect.',
        required=True,
    ),
    PropertyModel(
        label='Destination',
        name='destination',
        placeholder='Enter the destination address',
        property_type=prop_type.STR,
        description='Destination address.',
        required=True,
    ),
    PropertyModel(
        label='Active?',
        name='active',
        property_type=prop_type.BOOL,
        description='Set to True to active this redirect.',
        default=str_type.TRUE,
        required=True,
    ),
]

# Extensions
redirect_properties.extend(content_properties)

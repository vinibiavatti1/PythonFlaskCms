"""
Publish properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union


publish_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Publish'
    ),
    PropertyModel(
        label='Published?',
        name='published',
        property_type=prop_type.BOOL,
        description='Set to True to publish the content.',
        default=str_type.FALSE,
        required=True,
    ),
]

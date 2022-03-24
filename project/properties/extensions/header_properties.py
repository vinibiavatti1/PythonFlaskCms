"""
Header properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union


header_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Header'
    ),
    PropertyModel(
        name='header_title',
        label='Title',
        property_type=prop_type.STR,
        description='The title (H1) of the content',
        placeholder='Enter the title of the content',
        required=True,
    ),
]

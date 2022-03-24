"""
Content properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union


information_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Information'
    ),
    PropertyModel(
        label='Content URL',
        name='url',
        property_type=prop_type.INFO,
        description='Content access URL.',
    ),
]

"""
Schrmea properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union


# Properties
schema_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Schema'
    ),
    PropertyModel(
        label='Schema',
        name='schema',
        property_type=prop_type.CODE,
        description='The JSON schema that will be rendered to the page.',
        links=['https://www.schema.org/'],
        placeholder='Enter the JSON schema.',
    ),
]

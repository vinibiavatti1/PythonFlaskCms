"""
Navbar properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from project.properties.bases.component_properties import component_properties
from typing import Union

# Properties
navbar_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Navbar'
    ),
    PropertyModel(
        name='navbar_title',
        label='Title',
        property_type=prop_type.STR,
        description='Title that will be shown in navbar',
        placeholder='Enter the title',
        required=True,
    ),
]

# Extensions
navbar_properties.extend(component_properties)

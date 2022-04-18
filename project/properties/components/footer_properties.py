"""
Footer properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from project.properties.bases.component_properties import component_properties
from typing import Union

# Properties
footer_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Footer'
    ),
    PropertyModel(
        name='footer_title',
        label='Title',
        property_type=prop_type.STR,
        description='Title that will be shown in footer',
        placeholder='Enter the title',
        required=True,
    ),
    PropertyModel(
        name='footer_about',
        label='About',
        property_type=prop_type.TEXT,
        description='About text that will be shown in footer',
        placeholder='Enter the about text',
    ),
]

# Extensions
footer_properties.extend(component_properties)

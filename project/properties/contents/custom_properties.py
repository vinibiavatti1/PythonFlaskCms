"""
Custom page properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from typing import Union
from project.properties.bases.content_properties import content_properties


# Properties
custom_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Custom Page',
    ),
    PropertyModel(
        name='custom_html',
        label='Custom HTML code',
        property_type=prop_type.CODE,
        description='Custom HTML code that will be rendered to the page',
        placeholder='Enter the code',
        required=False,
    ),
    PropertyModel(
        name='custom_css',
        label='Custom CSS code',
        property_type=prop_type.CODE,
        description='Custom CSS (styles) code that will be inserted to the '
                    'page',
        placeholder='Enter the code',
        required=False,
    ),
    PropertyModel(
        name='custom_js',
        label='Custom JS code',
        property_type=prop_type.CODE,
        description='Custom Javascript code that will be executed in the page',
        placeholder='Enter the code',
        required=False,
    ),
]

# Extensions
custom_properties.extend(content_properties)

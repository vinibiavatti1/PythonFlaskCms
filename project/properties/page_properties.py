"""
Page records module.
"""
from typing import Union
from project.models.header_model import HeaderModel
from project.models.property_model import PropertyModel
from project.enums import property_types_enum as prop_type


page_properties: list[Union[HeaderModel, PropertyModel]] = [
    HeaderModel('General'),
    PropertyModel(
        name='h1',
        description='Primary header title',
        property_type=prop_type.STR,
    ),
    PropertyModel(
        name='h2',
        description='Secondary header title',
        property_type=prop_type.STR,
    ),
    # Add more here...
]

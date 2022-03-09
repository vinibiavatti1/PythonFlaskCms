"""
Page properties list.
"""
from typing import Union
from project.models.header_model import HeaderModel
from project.models.property_model import PropertyModel
from project.enums import property_types_enum as prop_type


###############################################################################
# Registry
###############################################################################


page_properties: list[Union[HeaderModel, PropertyModel]] = [
    HeaderModel('General'),
    PropertyModel(
        name='h1',
        description='Primary header title',
        field_type=prop_type.STRING,
    ),
    PropertyModel(
        name='h2',
        description='Secondary header title',
        field_type=prop_type.STRING,
    ),
    # Add more here...
]

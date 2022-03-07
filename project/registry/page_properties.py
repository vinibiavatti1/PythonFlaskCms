"""
Page properties list.
"""
from typing import Any, Union
from project.models.header_model import HeaderModel
from project.models.property_model import PropertyModel
from project.enums import field_types_enum as field


###############################################################################
# Registry
###############################################################################


page_properties: list[Union[HeaderModel, PropertyModel]] = [
    HeaderModel('General'),
    PropertyModel(
        name='h1',
        description='Primary header title',
        field_type=field.STRING,
    ),
    PropertyModel(
        name='h2',
        description='Secondary header title',
        field_type=field.STRING,
    ),
    # Add more here...
]

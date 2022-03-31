"""
Translation properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from typing import Union
from project.properties.bases.resource_properties import resource_properties


# Properties
translation_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Translation',
    ),
    PropertyModel(
        name='value',
        label='Value',
        property_type=prop_type.TEXT,
        description='Value of the translation.',
        placeholder='Enter the value of the translation',
        required=True,
    )
]

# Extensions
translation_properties.extend(resource_properties)

"""
Landing Page properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from typing import Union
from project.properties.bases.content_properties import content_properties


# Properties
landing_properties: list[Union[PropertyModel, HeaderModel]] = [
]

# Extensions
landing_properties.extend(content_properties)

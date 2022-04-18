"""
Component properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union
from project.properties.extensions.main_properties import main_properties
from project.properties.extensions.active_properties import active_properties


component_properties: list[Union[PropertyModel, HeaderModel]] = [
]

# Extensions
component_properties.extend(main_properties)

"""
Home page properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from typing import Union
from project.properties.bases.page_properties import page_properties


# Properties
home_page_properties: list[Union[PropertyModel, HeaderModel]] = [
]

# Extensions
home_page_properties.extend(page_properties)

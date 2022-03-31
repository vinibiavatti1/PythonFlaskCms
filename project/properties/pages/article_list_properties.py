"""
Article List properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from typing import Union
from project.properties.bases.page_properties import page_properties


# Properties
article_list_properties: list[Union[PropertyModel, HeaderModel]] = [
]

# Extensions
article_list_properties.extend(page_properties)

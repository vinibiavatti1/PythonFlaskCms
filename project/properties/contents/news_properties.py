"""
News properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from typing import Union
from project.properties.bases.content_properties import content_properties


# Properties
news_properties: list[Union[PropertyModel, HeaderModel]] = [
]

# Extensions
news_properties.extend(content_properties)

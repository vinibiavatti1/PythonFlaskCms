"""
Content properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union
from project.properties.main_properties import main_properties
from project.properties.extensions.list_properties import list_properties
from project.properties.extensions.seo_properties import seo_properties
from project.properties.extensions.sitemap_properties import sitemap_properties
from project.properties.extensions.url_properties import url_properties
from project.properties.extensions.publish_properties import publish_properties


content_properties: list[Union[PropertyModel, HeaderModel]] = [
]

# Extensions
content_properties.extend(publish_properties)
content_properties.extend(url_properties)
content_properties.extend(list_properties)
content_properties.extend(seo_properties)
content_properties.extend(sitemap_properties)

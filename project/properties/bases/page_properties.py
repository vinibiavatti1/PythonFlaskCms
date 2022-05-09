"""
Page properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union
from project.properties.extensions.seo_properties import seo_properties
from project.properties.extensions.sitemap_properties import sitemap_properties
from project.properties.extensions.url_properties import url_properties
from project.properties.extensions.schema_properties import schema_properties
from project.properties.extensions.security_properties import \
    security_properties


page_properties: list[Union[PropertyModel, HeaderModel]] = [
]

# Extensions
page_properties.extend(security_properties)
page_properties.extend(url_properties)
page_properties.extend(seo_properties)
page_properties.extend(sitemap_properties)
page_properties.extend(schema_properties)

"""
Article List properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.properties.extensions.publish_properties import publish_properties
from project.properties.extensions.seo_properties import seo_properties
from project.properties.extensions.sitemap_properties import sitemap_properties
from project.properties.extensions.access_properties import access_properties
from project.enums import property_types_enum as prop_type
from typing import Union


# Properties
article_list_properties: list[Union[PropertyModel, HeaderModel]] = [
]

# Extensions
article_list_properties.extend(publish_properties)
article_list_properties.extend(seo_properties)
article_list_properties.extend(sitemap_properties)
article_list_properties.extend(access_properties)

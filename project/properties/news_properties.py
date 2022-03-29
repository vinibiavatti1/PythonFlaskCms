"""
News properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from typing import Union
from project.properties.extensions.seo_properties import seo_properties
from project.properties.extensions.sitemap_properties import sitemap_properties
from project.properties.extensions.content_properties import content_properties
from project.properties.extensions.publish_properties import publish_properties
from project.properties.extensions.access_properties import access_properties
from project.properties.extensions.list_properties import list_properties
from project.properties.extensions.info_properties import info_properties


# Properties
news_properties: list[Union[PropertyModel, HeaderModel]] = [
]

# Extensions
news_properties.extend(content_properties)
news_properties.extend(publish_properties)
news_properties.extend(list_properties)
news_properties.extend(info_properties)
news_properties.extend(seo_properties)
news_properties.extend(sitemap_properties)
news_properties.extend(access_properties)

"""
Landing Page properties configuration.
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
from project.properties.extensions.info_properties import info_properties


# Properties
landing_page_properties: list[Union[PropertyModel, HeaderModel]] = [
]

# Extensions
landing_page_properties.extend(content_properties)
landing_page_properties.extend(publish_properties)
landing_page_properties.extend(info_properties)
landing_page_properties.extend(seo_properties)
landing_page_properties.extend(sitemap_properties)
landing_page_properties.extend(access_properties)

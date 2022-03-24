"""
Article properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.properties.extensions.seo_properties import seo_properties
from project.properties.extensions.sitemap_properties import sitemap_properties
from project.properties.extensions.content_properties import content_properties
from project.properties.extensions.access_properties import access_properties
from project.properties.extensions.list_properties import list_properties
from project.properties.extensions.information_properties \
    import information_properties
from project.enums import property_types_enum as prop_type
from typing import Union


# Properties
article_properties: list[Union[PropertyModel, HeaderModel]] = [
]

# Extensions
article_properties.extend(content_properties)
article_properties.extend(list_properties)
article_properties.extend(information_properties)
article_properties.extend(seo_properties)
article_properties.extend(sitemap_properties)
article_properties.extend(access_properties)

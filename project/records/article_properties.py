"""
Article properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.records.seo_properties import seo_properties
from project.records.sitemap_properties import sitemap_properties
from typing import Union


# Properties
article_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Article'
    ),
    # Add more...
]

# Extensions
article_properties.extend(seo_properties)
article_properties.extend(sitemap_properties)

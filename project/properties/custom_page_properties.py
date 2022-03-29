"""
Custom page properties configuration.
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
custom_page_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Custom Page',
    ),
    PropertyModel(
        name='custom_html',
        label='Custom HTML code',
        property_type=prop_type.CODE,
        description='Custom HTML code that will be rendered to the page',
        placeholder='Enter the code',
        required=False,
    ),
    PropertyModel(
        name='custom_css',
        label='Custom CSS code',
        property_type=prop_type.CODE,
        description='Custom CSS (styles) code that will be inserted to the '
                    'page',
        placeholder='Enter the code',
        required=False,
    ),
    PropertyModel(
        name='custom_js',
        label='Custom JS code',
        property_type=prop_type.CODE,
        description='Custom Javascript code that will be executed in the page',
        placeholder='Enter the code',
        required=False,
    ),
]

# Extensions
custom_page_properties.extend(content_properties)
custom_page_properties.extend(publish_properties)
custom_page_properties.extend(info_properties)
custom_page_properties.extend(seo_properties)
custom_page_properties.extend(sitemap_properties)
custom_page_properties.extend(access_properties)

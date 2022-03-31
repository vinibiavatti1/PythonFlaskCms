"""
Post properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from typing import Union
from project.properties.bases.content_properties import content_properties


# Properties
post_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='Post'
    ),
    PropertyModel(
        name='post_title',
        label='Post Title',
        property_type=prop_type.STR,
        description='The title (H1) of the blog post',
        placeholder='Enter the title of the post',
        required=True,
    ),
    PropertyModel(
        name='post_content',
        label='Post Content',
        property_type=prop_type.RICH_TEXT,
        description='Content of the blog post',
        placeholder='Enter the content of the post',
        required=True,
    ),
]

# Extensions
post_properties.extend(content_properties)

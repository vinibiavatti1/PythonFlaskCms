"""
SEO properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union


seo_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='SEO'
    ),
    PropertyModel(
        label='Title',
        name='seo_title',
        property_type=prop_type.STR,
        description='Resource title that will be used to title tag.',
        placeholder='Enter the resource title',
        required=False,
    ),
    PropertyModel(
        label='Author',
        name='seo_author',
        property_type=prop_type.STR,
        description='Resource author that will be used to meta '
                    'author tag.',
        placeholder='Enter the resource author name',
        required=False,
    ),
    PropertyModel(
        label='Description',
        name='seo_description',
        property_type=prop_type.TEXT,
        description='Resource description that will be used to meta '
                    'description tag.',
        placeholder='Enter the resource description',
        required=False,
    ),
    PropertyModel(
        label='Keywords',
        name='seo_keywords',
        property_type=prop_type.TEXT,
        description='Resource keywords that will be used to meta.'
                    'keywords tag. (Separate with comma (,)).',
        placeholder='Enter the resource keywords separated by comma (,)',
        required=False,
    ),
    PropertyModel(
        label='Canonical URL',
        name='seo_canonical_url',
        property_type=prop_type.URL,
        description='Resource canonical url that will be used to link '
                    'canonical tag.',
        placeholder='Enter the canonical url',
        required=False,
    ),
]

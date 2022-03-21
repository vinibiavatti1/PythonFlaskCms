"""
Content properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union


content_properties: list[Union[PropertyModel, HeaderModel]] = [

    ###########################################################################
    # Content
    ###########################################################################

    HeaderModel(
        title='Content'
    ),
    PropertyModel(
        label='Name',
        name='name',
        placeholder='Enter the content name',
        property_type=prop_type.KEY,
        description='Name of the content.',
        required=True,
    ),
    PropertyModel(
        label='Published?',
        name='published',
        property_type=prop_type.BOOL,
        description='Set to True to publish the content.',
        default=str_type.FALSE,
        required=True,
    ),
    PropertyModel(
        label='Show in lists?',
        name='show_in_lists',
        property_type=prop_type.BOOL,
        description='Set to True to show this content in the list pages.',
        default=str_type.TRUE,
        required=True,
    ),
    PropertyModel(
        label='Private?',
        name='private',
        property_type=prop_type.BOOL,
        description='Set to True to require user authentication to access '
                    'this content.',
        default=str_type.FALSE,
        required=True,
    ),

    ###########################################################################
    # Information
    ###########################################################################

    HeaderModel(
        title='Information'
    ),
    PropertyModel(
        label='Content URL',
        name='url',
        property_type=prop_type.INFO,
        description='Content access URL.',
    ),
]

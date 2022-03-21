"""
FAQ properties configuration.
"""
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type
from typing import Union


# Properties
faq_properties: list[Union[PropertyModel, HeaderModel]] = [
    HeaderModel(
        title='FAQ'
    ),
    PropertyModel(
        name='faq_question',
        label='Question',
        property_type=prop_type.TEXT,
        description='Question of the FAQ',
        placeholder='Enter the question of this FAQ',
        required=True,
    ),
    PropertyModel(
        name='faq_answer',
        label='Answer',
        property_type=prop_type.TEXT,
        description='Answer of the FAQ',
        placeholder='Enter the question of this FAQ',
        required=True,
    ),
    PropertyModel(
        name='faq_category',
        label='Category',
        property_type=prop_type.STR,
        description='Category of the FAQ',
        placeholder='Enter the category of this FAQ',
        required=False,
    ),
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
        default=str_type.TRUE,
        required=True,
    ),
]

"""
Properties list.
"""
from typing import Any, Union
from project.models.header_model import HeaderModel
from project.models.property_model import PropertyModel
from project.enums import field_types_enum as field


###############################################################################
# Registry
###############################################################################


properties: list[Union[HeaderModel, PropertyModel]] = [

    ###########################################################################
    # Website
    ###########################################################################

    HeaderModel('Website'),
    PropertyModel(
        name='website_title',
        description='Website title. This title will be used to navbars, '
                    'SEO titles, etc.',
        field_type=field.STRING,
        required=True,
        default='Website',
    ),
    PropertyModel(
        name='index_page',
        description='Initial page name of website. The user will be '
                    'redirected when the root URL (/) is accessed.',
        field_type=field.STRING,
        required=True,
        default='homepage',
    ),

    ###########################################################################
    # SEO
    ###########################################################################

    HeaderModel('SEO'),
    PropertyModel(
        name='seo_default_title',
        description='Default SEO title. It will be used if no '
                    'page title was specified.',
        field_type=field.STRING,
    ),
    PropertyModel(
        name='seo_default_description',
        description='Default SEO description. It will be used if no '
                    'page description was specified.',
        field_type=field.TEXT,
    ),
    PropertyModel(
        name='seo_default_keywords',
        description='Default SEO keywords. It will be used if no '
                    'page keywords was specified. Use comma (,) to separate.',
        field_type=field.TEXT,
    ),
    PropertyModel(
        name='seo_default_author',
        description='Default SEO author. It will be used if no '
                    'page author was specified.',
        field_type=field.TEXT,
    ),
    PropertyModel(
        name='seo_title_template',
        description='SEO title template. Use {{WEBSITE_TITLE}} to print the '
                    'website title and {{PAGE_TITLE}} to print the page '
                    'title.',
        field_type=field.TEXT,
        required=True,
        default='{{WEBSITE_TITLE}} / {{PAGE_TITLE}}',
    ),

    ###########################################################################
    # Scripts
    ###########################################################################

    HeaderModel('Scripts'),
    PropertyModel(
        name='head_script',
        description='Javascript script that will be inserted into <head> tag.',
        field_type=field.CODE,
    ),
    PropertyModel(
        name='body_script',
        description='Javascript script that will be inserted into <body> tag.',
        field_type=field.CODE,
    ),
]

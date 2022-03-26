"""
Properties records module.
"""
from typing import Union
from project.models.header_model import HeaderModel
from project.models.property_model import PropertyModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type


property_records: list[Union[HeaderModel, PropertyModel]] = [

    ###########################################################################
    # Website
    ###########################################################################

    HeaderModel(
        title='Website'
    ),
    PropertyModel(
        name='website_title',
        label='Website Title',
        description='Website title. This title will be used to navbars, '
                    'SEO titles, etc.',
        property_type=prop_type.STR,
        required=True,
        default='Website',
    ),
    PropertyModel(
        name='index_page',
        label='Index Page',
        description='Initial page name of website. The user will be '
                    'redirected when the root URL (/) is accessed.',
        property_type=prop_type.STR,
        required=True,
        default='homepage',
    ),
    PropertyModel(
        name='favicon_url',
        label='Favicon URL',
        description='Favicon URL that will be used for all pages',
        property_type=prop_type.STR,
        required=True,
        default='/static/favicons/favicon-32x32.png',
    ),
    PropertyModel(
        name='charset',
        label='Charset',
        description='Charset used in website',
        property_type=prop_type.STR,
        required=True,
        default='UTF-8',
    ),
    PropertyModel(
        name='responsive',
        label='Responsive',
        description='Adaptate website for small screens (mobiles, tablets, '
                    '...)',
        property_type=prop_type.BOOL,
        required=True,
        default=str_type.TRUE,
    ),

    ###########################################################################
    # SEO
    ###########################################################################

    HeaderModel(
        title='SEO'
    ),
    PropertyModel(
        name='seo_default_title',
        label='Default page title',
        description='Default SEO title. It will be used if no '
                    'page title was specified.',
        property_type=prop_type.STR,
    ),
    PropertyModel(
        name='seo_default_description',
        label='Default meta description',
        description='Default SEO description. It will be used if no '
                    'page description was specified.',
        property_type=prop_type.TEXT,
    ),
    PropertyModel(
        name='seo_default_keywords',
        label='Default Keywords',
        description='Default SEO keywords. It will be used if no '
                    'page keywords was specified. Use comma (,) to separate.',
        property_type=prop_type.TEXT,
    ),
    PropertyModel(
        name='seo_default_author',
        label='Default author',
        description='Default SEO author. It will be used if no '
                    'page author was specified.',
        property_type=prop_type.TEXT,
    ),
    PropertyModel(
        name='seo_title_template',
        label='Page title template',
        description='SEO title template. Use {{WEBSITE_TITLE}} to print the '
                    'website title and {{PAGE_TITLE}} to print the page '
                    'title.',
        property_type=prop_type.TEXT,
        default='{{WEBSITE_TITLE}} / {{PAGE_TITLE}}',
    ),

    ###########################################################################
    # Scripts
    ###########################################################################

    HeaderModel(
        title='Scripts'
    ),
    PropertyModel(
        name='head_script',
        label='Head script',
        description='Javascript script that will be inserted into <head> tag.',
        property_type=prop_type.CODE,
    ),
    PropertyModel(
        name='body_script',
        label='Body script',
        description='Javascript script that will be inserted into <body> tag.',
        property_type=prop_type.CODE,
    ),

    ###########################################################################
    # reCaptcha
    ###########################################################################

    HeaderModel(
        title='ReCaptcha'
    ),
    PropertyModel(
        name='recaptcha_enabled',
        label='ReCaptcha enabled',
        description='Enables the Google reCaptcha v3 in the website.',
        property_type=prop_type.BOOL,
        default=str_type.FALSE,
    ),
    PropertyModel(
        name='recaptcha_site_key',
        label='ReCaptcha site key',
        description='ReCaptcha site key.',
        property_type=prop_type.TEXT,
        default='6LfoMNgdAAAAAFC-FumFY8ga7QGAhBlPaOb0xBdH',
    ),
    PropertyModel(
        name='recaptcha_secret_key',
        label='ReCaptcha secret key',
        description='ReCaptcha secret key.',
        property_type=prop_type.TEXT,
        default='6LfoMNgdAAAAAEu51riSXQK5Pkcda8wf3gp5mNRk',
    ),
    PropertyModel(
        name='recaptcha_threshold',
        label='ReCaptcha threshold',
        description='ReCaptcha threshold 0.0 ~ 1.0.',
        property_type=prop_type.REAL,
        default='0.5'
    ),

    ###########################################################################
    # Google
    ###########################################################################

    HeaderModel(
        title='Google'
    ),
    PropertyModel(
        name='google_api_key',
        label='Google API Key',
        description='API Key for Google resources.',
        property_type=prop_type.TEXT,
    ),

    ###########################################################################
    # E-mail
    ###########################################################################

    HeaderModel(
        title='E-mail'
    ),
    PropertyModel(
        name='email_enabled',
        label='Email enabled',
        description='Enable email sending.',
        property_type=prop_type.BOOL,
        default=str_type.FALSE,
    ),
    PropertyModel(
        name='email_smtp',
        label='Email SMPT',
        description='Simple Mail Transfer Protocol Domain.',
        property_type=prop_type.STR,
    ),
    PropertyModel(
        name='email_port',
        label='Email port',
        description='Port of SMTP.',
        property_type=prop_type.INTEGER,
    ),
    PropertyModel(
        name='email_ssl',
        label='Email SSL',
        description='Set True if SMTP is SSL, False to TLS.',
        property_type=prop_type.BOOL,
        default=str_type.TRUE,
    ),
    PropertyModel(
        name='email_login',
        label='Email login',
        description='SMTP user login.',
        property_type=prop_type.STR,
    ),
    PropertyModel(
        name='email_password',
        label='Email password',
        description='SMTP user password.',
        property_type=prop_type.PASSWORD,
    ),
    PropertyModel(
        name='email_charset',
        label='Email charset',
        description='SMTP charset.',
        property_type=prop_type.STR,
        default='UTF-8',
    ),

    ###########################################################################
    # Formats
    ###########################################################################

    HeaderModel(
        title='Formats'
    ),
    PropertyModel(
        name='date_format',
        label='Date format',
        description='Format of the date. Reference: https://strftime.org/',
        property_type=prop_type.STR,
        default='%Y-%m-%d',
    ),
    PropertyModel(
        name='datetime_format',
        label='Datetime format',
        description='Format of the datetime. Reference: https://strftime.org/',
        property_type=prop_type.STR,
        default='%Y-%m-%d %H:%M:%S',
    ),

    ###########################################################################
    # Cookies
    ###########################################################################

    HeaderModel(
        title='Cookies'
    ),
    PropertyModel(
        name='cookie_policy_enabled',
        label='Cookie policy enabled',
        description='Enables cookie policy modal.',
        property_type=prop_type.BOOL,
        default=str_type.TRUE,
    ),

    ###########################################################################
    # Media
    ###########################################################################

    HeaderModel(
        title='Media'
    ),
    PropertyModel(
        name='media_page_size',
        label='Meida page size',
        description='The size of the media list page.',
        property_type=prop_type.INTEGER,
        default='60',
        required=True
    ),
]

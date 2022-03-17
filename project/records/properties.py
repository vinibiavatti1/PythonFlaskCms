"""
Properties records module.
"""
from typing import Union
from project.models.header_model import HeaderModel
from project.models.property_model import PropertyModel
from project.enums import property_types_enum as prop_type
from project.enums import string_types_enum as str_type


properties: list[Union[HeaderModel, PropertyModel]] = [

    ###########################################################################
    # Website
    ###########################################################################

    HeaderModel('Website'),
    PropertyModel(
        name='website_title',
        description='Website title. This title will be used to navbars, '
                    'SEO titles, etc.',
        property_type=prop_type.STRING,
        required=True,
        default='Website',
    ),
    PropertyModel(
        name='index_page',
        description='Initial page name of website. The user will be '
                    'redirected when the root URL (/) is accessed.',
        property_type=prop_type.STRING,
        required=True,
        default='homepage',
    ),
    PropertyModel(
        name='favicon_url',
        description='Favicon URL that will be used for all pages',
        property_type=prop_type.STRING,
        required=True,
        default='/static/medias/favicon-32x32.png',
    ),
    PropertyModel(
        name='charset',
        description='Charset used in website',
        property_type=prop_type.STRING,
        required=True,
        default='UTF-8',
    ),
    PropertyModel(
        name='responsive',
        description='Adaptate website for small screens (mobiles, tablets, '
                    '...)',
        property_type=prop_type.BOOL,
        required=True,
        default=str_type.TRUE,
    ),

    ###########################################################################
    # SEO
    ###########################################################################

    HeaderModel('SEO'),
    PropertyModel(
        name='seo_default_title',
        description='Default SEO title. It will be used if no '
                    'page title was specified.',
        property_type=prop_type.STRING,
    ),
    PropertyModel(
        name='seo_default_description',
        description='Default SEO description. It will be used if no '
                    'page description was specified.',
        property_type=prop_type.TEXT,
    ),
    PropertyModel(
        name='seo_default_keywords',
        description='Default SEO keywords. It will be used if no '
                    'page keywords was specified. Use comma (,) to separate.',
        property_type=prop_type.TEXT,
    ),
    PropertyModel(
        name='seo_default_author',
        description='Default SEO author. It will be used if no '
                    'page author was specified.',
        property_type=prop_type.TEXT,
    ),
    PropertyModel(
        name='seo_title_template',
        description='SEO title template. Use {{WEBSITE_TITLE}} to print the '
                    'website title and {{PAGE_TITLE}} to print the page '
                    'title.',
        property_type=prop_type.TEXT,
        default='{{WEBSITE_TITLE}} / {{PAGE_TITLE}}',
    ),

    ###########################################################################
    # Scripts
    ###########################################################################

    HeaderModel('Scripts'),
    PropertyModel(
        name='head_script',
        description='Javascript script that will be inserted into <head> tag.',
        property_type=prop_type.CODE,
    ),
    PropertyModel(
        name='body_script',
        description='Javascript script that will be inserted into <body> tag.',
        property_type=prop_type.CODE,
    ),
    PropertyModel(
        name='noscript_message',
        description='Message that will be shown when user does not have '
                    'javascript enabled in his browser.',
        property_type=prop_type.TEXT,
        default='You need Javascript enabled to use this website!',
    ),
    PropertyModel(
        name='noscript_link_label',
        description='Label of the link to redirect user to information of '
                    'scripts',
        property_type=prop_type.STRING,
        default='Info...',
    ),

    ###########################################################################
    # reCaptcha
    ###########################################################################

    HeaderModel('reCaptcha'),
    PropertyModel(
        name='recaptcha_enabled',
        description='Enables the Google reCaptcha v3 in the website.',
        property_type=prop_type.BOOL,
        default=str_type.FALSE,
    ),
    PropertyModel(
        name='recaptcha_site_key',
        description='reCaptcha site key.',
        property_type=prop_type.TEXT,
        default='6LfoMNgdAAAAAFC-FumFY8ga7QGAhBlPaOb0xBdH',
    ),
    PropertyModel(
        name='recaptcha_secret_key',
        description='reCaptcha secret key.',
        property_type=prop_type.TEXT,
        default='6LfoMNgdAAAAAEu51riSXQK5Pkcda8wf3gp5mNRk',
    ),
    PropertyModel(
        name='recaptcha_threshold',
        description='reCaptcha threshold 0.0 to 1.0.',
        property_type=prop_type.REAL,
        default='0.5'
    ),

    ###########################################################################
    # Google
    ###########################################################################

    HeaderModel('Google'),
    PropertyModel(
        name='google_api_key',
        description='API Key for Google resources.',
        property_type=prop_type.TEXT,
    ),

    ###########################################################################
    # E-mail
    ###########################################################################

    HeaderModel('E-mail'),
    PropertyModel(
        name='email_enabled',
        description='Enable email sending.',
        property_type=prop_type.BOOL,
        default=str_type.FALSE,
    ),
    PropertyModel(
        name='email_smtp',
        description='Simple Mail Transfer Protocol Domain.',
        property_type=prop_type.STRING,
    ),
    PropertyModel(
        name='email_port',
        description='Port of SMTP.',
        property_type=prop_type.INTEGER,
    ),
    PropertyModel(
        name='email_ssl',
        description='Set True if SMTP is SSL, False to TLS.',
        property_type=prop_type.BOOL,
        default='1',
    ),
    PropertyModel(
        name='email_login',
        description='SMTP user login.',
        property_type=prop_type.STRING,
    ),
    PropertyModel(
        name='email_password',
        description='SMTP user password.',
        property_type=prop_type.PASSWORD,
    ),
    PropertyModel(
        name='email_charset',
        description='SMTP charset.',
        property_type=prop_type.STRING,
        default='UTF-8',
    ),

    ###########################################################################
    # Formats
    ###########################################################################

    HeaderModel('Formats'),
    PropertyModel(
        name='date_format',
        description='Format of the date. Reference: https://strftime.org/',
        property_type=prop_type.STRING,
        default='%Y-%m-%d',
    ),
    PropertyModel(
        name='datetime_format',
        description='Format of the datetime. Reference: https://strftime.org/',
        property_type=prop_type.STRING,
        default='%Y-%m-%d %H:%M:%S',
    ),

    ###########################################################################
    # Controllers
    ###########################################################################

    HeaderModel('Controllers'),
    PropertyModel(
        name='login_ctrl_active',
        description='Activate login controller.',
        property_type=prop_type.BOOL,
        default=str_type.TRUE,
    ),
    PropertyModel(
        name='blog_ctrl_active',
        description='Activate blog controller.',
        property_type=prop_type.BOOL,
        default=str_type.TRUE,
    ),
    PropertyModel(
        name='faq_ctrl_active',
        description='Activate FAQ controller.',
        property_type=prop_type.BOOL,
        default=str_type.TRUE,
    ),

    ###########################################################################
    # Cookies
    ###########################################################################

    HeaderModel('Cookies'),
    PropertyModel(
        name='cookie_policy_enabled',
        description='Enables cookie policy modal.',
        property_type=prop_type.BOOL,
        default=str_type.TRUE,
    ),
]

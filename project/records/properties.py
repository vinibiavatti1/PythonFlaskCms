"""
Properties records module.
"""
from typing import Union
from project.models.header_model import HeaderModel
from project.models.property_model import PropertyModel
from project.enums import property_types_enum as prop_type


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
        field_type=prop_type.STRING,
        required=True,
        default='Website',
    ),
    PropertyModel(
        name='index_page',
        description='Initial page name of website. The user will be '
                    'redirected when the root URL (/) is accessed.',
        field_type=prop_type.STRING,
        required=True,
        default='homepage',
    ),
    PropertyModel(
        name='favicon_url',
        description='Favicon URL that will be used for all pages',
        field_type=prop_type.STRING,
        required=True,
        default='/static/medias/favicon-32x32.png',
    ),
    PropertyModel(
        name='charset',
        description='Charset used in website',
        field_type=prop_type.STRING,
        required=True,
        default='UTF-8',
    ),
    PropertyModel(
        name='responsive',
        description='Adaptate website for small screens (mobiles, tablets, '
                    '...)',
        field_type=prop_type.BOOL,
        required=True,
        default=True,
    ),

    ###########################################################################
    # SEO
    ###########################################################################

    HeaderModel('SEO'),
    PropertyModel(
        name='seo_default_title',
        description='Default SEO title. It will be used if no '
                    'page title was specified.',
        field_type=prop_type.STRING,
    ),
    PropertyModel(
        name='seo_default_description',
        description='Default SEO description. It will be used if no '
                    'page description was specified.',
        field_type=prop_type.TEXT,
    ),
    PropertyModel(
        name='seo_default_keywords',
        description='Default SEO keywords. It will be used if no '
                    'page keywords was specified. Use comma (,) to separate.',
        field_type=prop_type.TEXT,
    ),
    PropertyModel(
        name='seo_default_author',
        description='Default SEO author. It will be used if no '
                    'page author was specified.',
        field_type=prop_type.TEXT,
    ),
    PropertyModel(
        name='seo_title_template',
        description='SEO title template. Use {{WEBSITE_TITLE}} to print the '
                    'website title and {{PAGE_TITLE}} to print the page '
                    'title.',
        field_type=prop_type.TEXT,
        default='{{WEBSITE_TITLE}} / {{PAGE_TITLE}}',
    ),

    ###########################################################################
    # Scripts
    ###########################################################################

    HeaderModel('Scripts'),
    PropertyModel(
        name='head_script',
        description='Javascript script that will be inserted into <head> tag.',
        field_type=prop_type.CODE,
    ),
    PropertyModel(
        name='body_script',
        description='Javascript script that will be inserted into <body> tag.',
        field_type=prop_type.CODE,
    ),
    PropertyModel(
        name='noscript_message',
        description='Message that will be shown when user does not have '
                    'javascript enabled in his browser.',
        field_type=prop_type.TEXT,
        default='You need Javascript enabled to use this website!',
    ),
    PropertyModel(
        name='noscript_link_label',
        description='Label of the link to redirect user to information of '
                    'scripts',
        field_type=prop_type.STRING,
        default='Info...',
    ),

    ###########################################################################
    # reCaptcha
    ###########################################################################

    HeaderModel('reCaptcha'),
    PropertyModel(
        name='recaptcha_enabled',
        description='Enables the Google reCaptcha v3 in the website.',
        field_type=prop_type.BOOL,
        default=False,
    ),
    PropertyModel(
        name='recaptcha_site_key',
        description='reCaptcha site key.',
        field_type=prop_type.TEXT,
        default='6LfoMNgdAAAAAFC-FumFY8ga7QGAhBlPaOb0xBdH',
    ),
    PropertyModel(
        name='recaptcha_secret_key',
        description='reCaptcha secret key.',
        field_type=prop_type.TEXT,
        default='6LfoMNgdAAAAAEu51riSXQK5Pkcda8wf3gp5mNRk',
    ),
    PropertyModel(
        name='recaptcha_threshold',
        description='reCaptcha threshold 0.0 to 1.0.',
        field_type=prop_type.REAL,
        default=0.5
    ),

    ###########################################################################
    # Google
    ###########################################################################

    HeaderModel('Google'),
    PropertyModel(
        name='google_api_key',
        description='API Key for Google resources.',
        field_type=prop_type.TEXT,
    ),

    ###########################################################################
    # E-mail
    ###########################################################################

    HeaderModel('E-mail'),
    PropertyModel(
        name='email_enabled',
        description='Enable email sending.',
        field_type=prop_type.BOOL,
        default=False,
    ),
    PropertyModel(
        name='email_smtp',
        description='Simple Mail Transfer Protocol Domain.',
        field_type=prop_type.STRING,
    ),
    PropertyModel(
        name='email_port',
        description='Port of SMTP.',
        field_type=prop_type.INTEGER,
    ),
    PropertyModel(
        name='email_ssl',
        description='Set True if SMTP is SSL, False to TLS.',
        field_type=prop_type.BOOL,
        default=True,
    ),
    PropertyModel(
        name='email_login',
        description='SMTP user login.',
        field_type=prop_type.STRING,
    ),
    PropertyModel(
        name='email_password',
        description='SMTP user password.',
        field_type=prop_type.PASSWORD,
    ),
    PropertyModel(
        name='email_charset',
        description='SMTP charset.',
        field_type=prop_type.STRING,
        default='UTF-8',
    ),

    ###########################################################################
    # Formats
    ###########################################################################

    HeaderModel('Formats'),
    PropertyModel(
        name='date_format',
        description='Format of the date. Reference: https://strftime.org/',
        field_type=prop_type.STRING,
        default='%Y-%m-%d',
    ),
    PropertyModel(
        name='datetime_format',
        description='Format of the datetime. Reference: https://strftime.org/',
        field_type=prop_type.STRING,
        default='%Y-%m-%d %H:%M:%S',
    ),

    ###########################################################################
    # Controllers
    ###########################################################################

    HeaderModel('Controllers'),
    PropertyModel(
        name='login_ctrl_active',
        description='Activate login controller.',
        field_type=prop_type.BOOL,
        default=True,
    ),
    PropertyModel(
        name='blog_ctrl_active',
        description='Activate blog controller.',
        field_type=prop_type.BOOL,
        default=True,
    ),
    PropertyModel(
        name='faq_ctrl_active',
        description='Activate FAQ controller.',
        field_type=prop_type.BOOL,
        default=True,
    ),

    ###########################################################################
    # Cookies
    ###########################################################################

    HeaderModel('Cookies'),
    PropertyModel(
        name='cookie_policy_enabled',
        description='Enables cookie policy modal.',
        field_type=prop_type.BOOL,
        default=True,
    ),
    PropertyModel(
        name='cookie_policy_title',
        description='Title of the cookie policy modal.',
        field_type=prop_type.STRING,
        default='Cookie Policy',
    ),
    PropertyModel(
        name='cookie_policy_content',
        description='Content that will be shown in cookie policy modal.',
        field_type=prop_type.TEXT,
        default='EN-US: We use cookies to improve user experience, and '
                'analyze website traffic. For these reasons, we may share '
                'your site usage data with our analytics partners. By '
                'clicking "Agree" you consent to store on your device all the '
                'technologies used in the application',
    ),
    PropertyModel(
        name='cookie_policy_agree',
        description='Agree button label. (Keep empty to disable)',
        field_type=prop_type.STRING,
        default='Agree',
    ),
    PropertyModel(
        name='cookie_policy_disagree',
        description='Disagree button label. (Keep empty to disable)',
        field_type=prop_type.STRING,
        default='Disagree',
    ),
    PropertyModel(
        name='cookie_policy_cancel',
        description='Cancel button label. (Keep empty to disable)',
        field_type=prop_type.STRING,
        default='Cancel',
    ),
]

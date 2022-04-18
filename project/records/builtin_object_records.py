"""
Builtin object records.
"""
from project.models.builtin_object_model import BuiltinObjectModel
from project.enums import string_types_enum as str_type
from project.enums import object_type_enum
from project.enums import object_subtype_enum


builtin_object_records: list[BuiltinObjectModel] = [

    ###########################################################################
    # Pages
    ###########################################################################

    BuiltinObjectModel(
        name='articles',
        object_type=object_type_enum.PAGE,
        object_subtype=object_subtype_enum.ARTICLE_PAGE,
        properties={
            'published': str_type.TRUE,
            'private': str_type.FALSE,
            'header_title': 'Articles',
            'seo_title': 'Articles',
            'seo_author': 'System',
            'seo_description': 'Articles list page',
            'seo_keywords': 'articles,list',
            'seo_canonical_url': '',
            'sitemap_active': str_type.TRUE,
            'sitemap_priority': '0.5',
            'sitemap_change_frequently': 'daily',
        },
    ),
    BuiltinObjectModel(
        name='events',
        object_type=object_type_enum.PAGE,
        object_subtype=object_subtype_enum.EVENT_PAGE,
        properties={
            'published': str_type.TRUE,
            'private': str_type.FALSE,
            'header_title': 'Events',
            'seo_title': 'Events',
            'seo_author': 'System',
            'seo_description': 'Events list page',
            'seo_keywords': 'events,list',
            'seo_canonical_url': '',
            'sitemap_active': str_type.TRUE,
            'sitemap_priority': '0.6',
            'sitemap_change_frequently': 'hourly',
        },
    ),
    BuiltinObjectModel(
        name='news',
        object_type=object_type_enum.PAGE,
        object_subtype=object_subtype_enum.NEWS_PAGE,
        properties={
            'published': str_type.TRUE,
            'private': str_type.FALSE,
            'header_title': 'News',
            'seo_title': 'News',
            'seo_author': 'System',
            'seo_description': 'News list page',
            'seo_keywords': 'news,list',
            'seo_canonical_url': '',
            'sitemap_active': str_type.TRUE,
            'sitemap_priority': '0.7',
            'sitemap_change_frequently': 'always',
        },
    ),
    BuiltinObjectModel(
        name='faqs',
        object_type=object_type_enum.PAGE,
        object_subtype=object_subtype_enum.FAQ_PAGE,
        properties={
            'published': str_type.TRUE,
            'private': str_type.FALSE,
            'header_title': 'FAQ',
            'seo_title': 'FAQ',
            'seo_author': 'System',
            'seo_description': 'FAQ list page',
            'seo_keywords': 'faq,questions,answers,list',
            'seo_canonical_url': '',
            'sitemap_active': str_type.TRUE,
            'sitemap_priority': '0.5',
            'sitemap_change_frequently': 'monthly',
        },
    ),
    BuiltinObjectModel(
        name='calendar',
        object_type=object_type_enum.PAGE,
        object_subtype=object_subtype_enum.CALENDAR_PAGE,
        properties={
            'published': str_type.TRUE,
            'private': str_type.FALSE,
            'header_title': 'Calendar',
            'seo_title': 'Calendar',
            'seo_author': 'System',
            'seo_description': 'Calendar page',
            'seo_keywords': 'calendar,events,page',
            'seo_canonical_url': '',
            'sitemap_active': str_type.TRUE,
            'sitemap_priority': '0.6',
            'sitemap_change_frequently': 'hourly',
        },
    ),
    BuiltinObjectModel(
        name='search',
        object_type=object_type_enum.PAGE,
        object_subtype=object_subtype_enum.SEARCH_PAGE,
        properties={
            'published': str_type.TRUE,
            'private': str_type.FALSE,
            'header_title': 'Search',
            'seo_title': 'Search',
            'seo_author': 'System',
            'seo_description': 'Search page',
            'seo_keywords': 'search,query,page',
            'seo_canonical_url': '',
            'sitemap_active': str_type.TRUE,
            'sitemap_priority': '0.0',
            'sitemap_change_frequently': 'never',
        },
    ),
    BuiltinObjectModel(
        name='login',
        object_type=object_type_enum.PAGE,
        object_subtype=object_subtype_enum.LOGIN_PAGE,
        properties={
            'published': str_type.TRUE,
            'private': str_type.FALSE,
            'header_title': 'Login',
            'seo_title': 'Login',
            'seo_author': 'System',
            'seo_description': 'Login page',
            'seo_keywords': 'login,authentication,page',
            'seo_canonical_url': '',
            'sitemap_active': str_type.TRUE,
            'sitemap_priority': '0.0',
            'sitemap_change_frequently': 'never',
        },
    ),
    BuiltinObjectModel(
        name='contact',
        object_type=object_type_enum.PAGE,
        object_subtype=object_subtype_enum.CONTACT_PAGE,
        properties={
            'published': str_type.TRUE,
            'private': str_type.FALSE,
            'header_title': 'Contact',
            'seo_title': 'Contact',
            'seo_author': 'System',
            'seo_description': 'Contact page',
            'seo_keywords': 'contact,location,page',
            'seo_canonical_url': '',
            'sitemap_active': str_type.TRUE,
            'sitemap_priority': '0.5',
            'sitemap_change_frequently': 'monthly',
        },
    ),
    BuiltinObjectModel(
        name='blog',
        object_type=object_type_enum.PAGE,
        object_subtype=object_subtype_enum.BLOG_PAGE,
        properties={
            'published': str_type.TRUE,
            'private': str_type.FALSE,
            'header_title': 'Blog',
            'seo_title': 'Blog',
            'seo_author': 'System',
            'seo_description': 'Blog page',
            'seo_keywords': 'blog,posts,page',
            'seo_canonical_url': '',
            'sitemap_active': str_type.TRUE,
            'sitemap_priority': '0.7',
            'sitemap_change_frequently': 'always',
        },
    ),

    ###########################################################################
    # Components
    ###########################################################################

    BuiltinObjectModel(
        name='navbar',
        object_type=object_type_enum.COMPONENT,
        object_subtype=object_subtype_enum.NAVBAR_COMPONENT,
        properties={},
    ),
    BuiltinObjectModel(
        name='footer',
        object_type=object_type_enum.COMPONENT,
        object_subtype=object_subtype_enum.FOOTER_COMPONENT,
        properties={},
    ),

    ###########################################################################
    # Resources
    ###########################################################################

    BuiltinObjectModel(
        name='cookie_policy_title',
        object_type=object_type_enum.RESOURCE,
        object_subtype=object_subtype_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'Cookie Policy',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='cookie_policy_content',
        object_type=object_type_enum.RESOURCE,
        object_subtype=object_subtype_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'We use cookies to improve user experience, and analyze '
                     'website traffic. For these reasons, we may share your '
                     'site usage data with our analytics partners. By '
                     'clicking "Agree" you consent to store on your device '
                     'all the technologies used in the application',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='cookie_policy_agree',
        object_type=object_type_enum.RESOURCE,
        object_subtype=object_subtype_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'Agree',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='cookie_policy_disagree',
        object_type=object_type_enum.RESOURCE,
        object_subtype=object_subtype_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'Disagree',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='cookie_policy_cancel',
        object_type=object_type_enum.RESOURCE,
        object_subtype=object_subtype_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'Cancel',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='error_not_found',
        object_type=object_type_enum.RESOURCE,
        object_subtype=object_subtype_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'The page was not found',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='error_unauthorized',
        object_type=object_type_enum.RESOURCE,
        object_subtype=object_subtype_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'You must authenticate to access this resource',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='error_bad_request',
        object_type=object_type_enum.RESOURCE,
        object_subtype=object_subtype_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'Error to process the request. Please, try again.',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='error_forbidden',
        object_type=object_type_enum.RESOURCE,
        object_subtype=object_subtype_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'You don\'t have access rights to access this content',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='error_internal_server',
        object_type=object_type_enum.RESOURCE,
        object_subtype=object_subtype_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'An internal server error occurred. Please, try again. '
                     'If the same error continues, contact the administrator.',
            'active': str_type.TRUE,
        },
    ),
]

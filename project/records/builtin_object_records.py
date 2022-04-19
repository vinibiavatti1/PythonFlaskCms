"""
Builtin object records.
"""
from project.models.builtin_object_model import BuiltinObjectModel
from project.enums import string_types_enum as str_type
from project.enums import object_enum
from project.enums import object_enum


builtin_object_records: list[BuiltinObjectModel] = [

    ###########################################################################
    # Folders
    ###########################################################################

    BuiltinObjectModel(
        name='Pages',
        object_type=object_enum.PAGES_FOLDER,
        properties={},
    ),
    BuiltinObjectModel(
        name='Components',
        object_type=object_enum.COMPONENTS_FOLDER,
        properties={},
    ),
    BuiltinObjectModel(
        name='Resources',
        object_type=object_enum.RESOURCES_FOLDER,
        properties={},
    ),
    BuiltinObjectModel(
        name='Translations',
        reference_name='Resources',
        object_type=object_enum.TRANSLATIONS_FOLDER,
        properties={},
    ),
    BuiltinObjectModel(
        name='Redirects',
        reference_name='Resources',
        object_type=object_enum.REDIRECTS_FOLDER,
        properties={},
    ),

    ###########################################################################
    # Pages
    ###########################################################################

    BuiltinObjectModel(
        name='Homepage',
        reference_name='Pages',
        object_type=object_enum.HOME_PAGE,
        properties={
            'published': str_type.TRUE,
            'private': str_type.FALSE,
            'header_title': 'Homepage',
            'seo_title': 'Homepage',
            'seo_author': 'System',
            'seo_description': 'Homepage',
            'seo_keywords': 'homepage',
            'seo_canonical_url': '',
            'sitemap_active': str_type.TRUE,
            'sitemap_priority': '0.5',
            'sitemap_change_frequently': 'daily',
        },
    ),
    BuiltinObjectModel(
        name='Articles',
        reference_name='Pages',
        object_type=object_enum.ARTICLE_PAGE,
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
        name='Events',
        reference_name='Pages',
        object_type=object_enum.EVENT_PAGE,
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
        name='News',
        reference_name='Pages',
        object_type=object_enum.NEWS_PAGE,
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
        name='Faqs',
        reference_name='Pages',
        object_type=object_enum.FAQ_PAGE,
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
        name='Calendar',
        reference_name='Pages',
        object_type=object_enum.CALENDAR_PAGE,
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
        name='Search',
        reference_name='Pages',
        object_type=object_enum.SEARCH_PAGE,
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
        name='Login',
        reference_name='Pages',
        object_type=object_enum.LOGIN_PAGE,
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
        name='Contact',
        reference_name='Pages',
        object_type=object_enum.CONTACT_PAGE,
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
        name='Blog',
        reference_name='Pages',
        object_type=object_enum.BLOG_PAGE,
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
        reference_name='Components',
        object_type=object_enum.NAVBAR_COMPONENT,
        properties={},
    ),
    BuiltinObjectModel(
        name='footer',
        reference_name='Components',
        object_type=object_enum.FOOTER_COMPONENT,
        properties={},
    ),

    ###########################################################################
    # Resources
    ###########################################################################

    BuiltinObjectModel(
        name='cookie_policy_title',
        reference_name='Translations',
        object_type=object_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'Cookie Policy',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='cookie_policy_content',
        reference_name='Translations',
        object_type=object_enum.TRANSLATION_RESOURCE,
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
        reference_name='Translations',
        object_type=object_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'Agree',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='cookie_policy_disagree',
        reference_name='Translations',
        object_type=object_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'Disagree',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='cookie_policy_cancel',
        reference_name='Translations',
        object_type=object_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'Cancel',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='error_not_found',
        reference_name='Translations',
        object_type=object_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'The page was not found',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='error_unauthorized',
        reference_name='Translations',
        object_type=object_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'You must authenticate to access this resource',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='error_bad_request',
        reference_name='Translations',
        object_type=object_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'Error to process the request. Please, try again.',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='error_forbidden',
        reference_name='Translations',
        object_type=object_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'You don\'t have access rights to access this content',
            'active': str_type.TRUE,
        },
    ),
    BuiltinObjectModel(
        name='error_internal_server',
        reference_name='Translations',
        object_type=object_enum.TRANSLATION_RESOURCE,
        properties={
            'value': 'An internal server error occurred. Please, try again. '
                     'If the same error continues, contact the administrator.',
            'active': str_type.TRUE,
        },
    ),
]

"""
Object records.
"""
from project.models.object_model import ObjectModel
from project.enums import object_enum

# Pages
from project.properties.pages.home_page_properties \
    import home_page_properties
from project.properties.pages.article_list_properties \
    import article_list_properties
from project.properties.pages.blog_properties \
    import blog_properties
from project.properties.pages.calendar_properties \
    import calendar_properties
from project.properties.pages.contact_properties \
    import contact_properties
from project.properties.pages.event_list_properties \
    import event_list_properties
from project.properties.pages.faq_list_properties \
    import faq_list_properties
from project.properties.pages.login_properties \
    import login_properties
from project.properties.pages.news_list_properties \
    import news_list_properties
from project.properties.pages.search_properties \
    import search_properties

# Contents
from project.properties.contents.article_properties \
    import article_properties
from project.properties.contents.custom_properties \
    import custom_properties
from project.properties.contents.event_properties \
    import event_properties
from project.properties.contents.landing_properties \
    import landing_properties
from project.properties.contents.news_properties \
    import news_properties
from project.properties.contents.post_properties \
    import post_properties

# Resources
from project.properties.resources.announcement_properties \
    import announcement_properties
from project.properties.resources.translation_properties \
    import translation_properties
from project.properties.resources.redirect_properties \
    import redirect_properties
from project.properties.resources.faq_properties import \
    faq_properties

# Components
from project.properties.components.footer_properties \
    import footer_properties
from project.properties.components.navbar_properties \
    import navbar_properties


object_records: list[ObjectModel] = [

    ###########################################################################
    # Folders
    ###########################################################################

    ObjectModel(
        name=object_enum.PAGES_FOLDER,
        description='Pages folder',
        icon='bi-folder',
        is_root=True,
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.ARTICLE_PAGE,
            object_enum.EVENT_PAGE,
            object_enum.NEWS_PAGE,
            object_enum.FAQ_PAGE,
            object_enum.CALENDAR_PAGE,
            object_enum.SEARCH_PAGE,
            object_enum.LOGIN_PAGE,
            object_enum.CONTACT_PAGE,
            object_enum.BLOG_PAGE,
        ],
    ),
    ObjectModel(
        name=object_enum.COMPONENTS_FOLDER,
        description='Components folder',
        icon='bi-folder',
        is_root=True,
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.NAVBAR_COMPONENT,
            object_enum.FOOTER_COMPONENT,
        ],
    ),
    ObjectModel(
        name=object_enum.RESOURCES_FOLDER,
        description='Resources folder',
        icon='bi-folder',
        is_root=True,
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.TRANSLATIONS_FOLDER,
            object_enum.ANNOUNCEMENTS_FOLDER,
            object_enum.REDIRECTS_FOLDER,
        ],
    ),
    ObjectModel(
        name=object_enum.TRANSLATIONS_FOLDER,
        description='Translations folder',
        icon='bi-folder',
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.TRANSLATION_RESOURCE,
        ],
    ),
    ObjectModel(
        name=object_enum.ANNOUNCEMENTS_FOLDER,
        description='Annoucements folder',
        icon='bi-folder',
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.ANNOUNCEMENT_RESOURCE,
        ],
    ),
    ObjectModel(
        name=object_enum.REDIRECTS_FOLDER,
        description='Redirects folder',
        icon='bi-folder',
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.REDIRECT_RESOURCE,
        ],
    ),

    ###########################################################################
    # Pages
    ###########################################################################

    ObjectModel(
        name=object_enum.HOME_PAGE,
        description='Home page',
        icon='bi-house',
        is_content=True,
        properties=home_page_properties,
        allow_actions=False,
        template='homepage.html',
        children=[
            object_enum.HEADER_BLOCK
        ],
    ),
    ObjectModel(
        name=object_enum.ARTICLE_PAGE,
        description='Article list page',
        icon='bi-file-earmark-post',
        is_content=True,
        properties=article_list_properties,
        allow_actions=False,
        template='article_list.html',
        children=[
            object_enum.ARTICLE_CONTENT
        ],
    ),
    ObjectModel(
        name=object_enum.EVENT_PAGE,
        description='Event list page',
        icon='bi-file-earmark-medical',
        is_content=True,
        properties=event_list_properties,
        allow_actions=False,
        template='event_list.html',
        children=[
            object_enum.EVENT_CONTENT
        ],
    ),
    ObjectModel(
        name=object_enum.NEWS_PAGE,
        description='News list page',
        icon='bi-file-earmark-easel',
        is_content=True,
        properties=news_list_properties,
        allow_actions=False,
        template='news_list.html',
        children=[
            object_enum.NEWS_CONTENT
        ],
    ),
    ObjectModel(
        name=object_enum.FAQ_PAGE,
        description='FAQ list page',
        icon='bi-file-earmark-text',
        is_content=True,
        properties=faq_list_properties,
        allow_actions=False,
        template='faq_list.html',
        children=[
            object_enum.FAQ_RESOURCE
        ],
    ),
    ObjectModel(
        name=object_enum.CALENDAR_PAGE,
        description='Calendar page',
        icon='bi-calendar',
        is_content=True,
        properties=calendar_properties,
        allow_actions=False,
        template='calendar.html',
        children=[],
    ),
    ObjectModel(
        name=object_enum.SEARCH_PAGE,
        description='Search page',
        icon='bi-search',
        is_content=True,
        properties=search_properties,
        allow_actions=False,
        template='search.html',
        children=[],
    ),
    ObjectModel(
        name=object_enum.LOGIN_PAGE,
        description='Login page',
        icon='bi-key',
        is_content=True,
        properties=login_properties,
        allow_actions=False,
        template='login.html',
        children=[],
    ),
    ObjectModel(
        name=object_enum.CONTACT_PAGE,
        description='Contact page',
        icon='bi-file-earmark-person',
        is_content=True,
        properties=contact_properties,
        allow_actions=False,
        template='contact.html',
        children=[],
    ),
    ObjectModel(
        name=object_enum.BLOG_PAGE,
        description='Blog page',
        icon='bi-postage',
        is_content=True,
        properties=blog_properties,
        allow_actions=False,
        template='blog.html',
        children=[],
    ),

    ###########################################################################
    # Contents
    ###########################################################################

    ObjectModel(
        name=object_enum.ARTICLE_CONTENT,
        description='Article content',
        icon='bi-files',
        is_content=True,
        properties=article_properties,
        allow_actions=True,
        template='article.html',
        children=[
            object_enum.HEADER_BLOCK
        ],
    ),
    ObjectModel(
        name=object_enum.EVENT_CONTENT,
        description='Event content',
        icon='bi-calendar-event',
        is_content=True,
        properties=event_properties,
        allow_actions=True,
        template='event.html',
        children=[
            object_enum.HEADER_BLOCK
        ],
    ),
    ObjectModel(
        name=object_enum.NEWS_CONTENT,
        description='News content',
        icon='bi-newspaper',
        is_content=True,
        properties=news_properties,
        allow_actions=True,
        template='news.html',
        children=[
            object_enum.HEADER_BLOCK
        ],
    ),
    ObjectModel(
        name=object_enum.POST_CONTENT,
        description='Post content',
        icon='bi-pin-angle',
        is_content=True,
        properties=post_properties,
        allow_actions=True,
        template='post.html',
        children=[
            object_enum.HEADER_BLOCK
        ],
    ),
    ObjectModel(
        name=object_enum.CUSTOM_CONTENT,
        description='Custom content',
        icon='bi-filetype-html',
        is_content=True,
        properties=custom_properties,
        allow_actions=True,
        template='custom.html',
        children=[],
    ),

    ###########################################################################
    # Components
    ###########################################################################

    ObjectModel(
        name=object_enum.NAVBAR_COMPONENT,
        description='Navbar component',
        icon='bi-window',
        is_content=False,
        properties=navbar_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),
    ObjectModel(
        name=object_enum.FOOTER_COMPONENT,
        description='Footer component',
        icon='bi-window-desktop',
        is_content=False,
        properties=footer_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),

    ###########################################################################
    # Resources
    ###########################################################################

    ObjectModel(
        name=object_enum.TRANSLATION_RESOURCE,
        description='Translation resource',
        icon='bi-translate',
        is_content=False,
        properties=translation_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),
    ObjectModel(
        name=object_enum.FAQ_RESOURCE,
        description='FAQ resource',
        icon='bi-question-circle',
        is_content=False,
        properties=faq_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),
    ObjectModel(
        name=object_enum.REDIRECT_RESOURCE,
        description='Redirect resource',
        icon='bi-signpost-split',
        is_content=False,
        properties=redirect_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),
    ObjectModel(
        name=object_enum.ANNOUNCEMENT_RESOURCE,
        description='Annoucement resource',
        icon='bi-megaphone',
        is_content=False,
        properties=announcement_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),
]

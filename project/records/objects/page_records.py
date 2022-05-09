"""
Page records.
"""
from project.models.object_model import ObjectModel
from project.enums import object_enum
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


page_records: list[ObjectModel] = [
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
]

"""
Context records module.
"""
from project.models.page_type_model import PageTypeModel
from project.enums import object_subtype_enum
from project.models.property_model import PropertyModel
from project.enums import string_types_enum as str_type
from project.properties.pages.article_list_properties import \
    article_list_properties
from project.properties.pages.blog_properties import \
    blog_properties
from project.properties.pages.calendar_properties import \
    calendar_properties
from project.properties.pages.contact_properties import \
    contact_properties
from project.properties.pages.event_list_properties import \
    event_list_properties
from project.properties.pages.faq_list_properties import \
    faq_list_properties
from project.properties.pages.login_properties import \
    login_properties
from project.properties.pages.news_list_properties import \
    news_list_properties
from project.properties.pages.search_properties import \
    search_properties


page_type_records: list[PageTypeModel] = [
    PageTypeModel(
        label='Article List',
        name=object_subtype_enum.ARTICLE_PAGE,
        template='article_list.html',
        icon='bi-file-earmark-post',
        properties=article_list_properties,
    ),
    PageTypeModel(
        label='Event List',
        name=object_subtype_enum.EVENT_PAGE,
        template='event_list.html',
        icon='bi-file-earmark-medical',
        properties=event_list_properties,
    ),
    PageTypeModel(
        label='News List',
        name=object_subtype_enum.NEWS_PAGE,
        template='news_list.html',
        icon='bi-file-earmark-easel',
        properties=news_list_properties,
    ),
    PageTypeModel(
        label='Faq List',
        name=object_subtype_enum.FAQ_PAGE,
        template='faq_list.html',
        icon='bi-file-earmark-text',
        properties=faq_list_properties,
    ),
    PageTypeModel(
        label='Calendar',
        name=object_subtype_enum.CALENDAR_PAGE,
        template='calendar.html',
        icon='bi-calendar',
        properties=calendar_properties,
    ),
    PageTypeModel(
        label='Search',
        name=object_subtype_enum.SEARCH_PAGE,
        template='search.html',
        icon='bi-search',
        properties=search_properties,
    ),
    PageTypeModel(
        label='Login',
        name=object_subtype_enum.LOGIN_PAGE,
        template='login.html',
        icon='bi-key',
        properties=login_properties,
    ),
    PageTypeModel(
        label='Contact',
        name=object_subtype_enum.CONTACT_PAGE,
        template='contact.html',
        icon='bi-file-earmark-person',
        properties=contact_properties,
    ),
    PageTypeModel(
        label='Blog',
        name=object_subtype_enum.BLOG_PAGE,
        template='blog.html',
        icon='bi-postage',
        properties=blog_properties,
    ),
    # Add more...
]

"""
Context records module.
"""
from project.models.page_type_model import PageTypeModel
from project.enums import object_subtype_enum


page_type_records: list[PageTypeModel] = [
    PageTypeModel(
        label='Article List',
        name=object_subtype_enum.ARTICLE_PAGE,
        template='article_list.html',
        icon='bi-file-earmark-post',
        properties=[],
    ),
    PageTypeModel(
        label='Event List',
        name=object_subtype_enum.EVENT_PAGE,
        template='event_list.html',
        icon='bi-file-earmark-medical',
        properties=[],
    ),
    PageTypeModel(
        label='News List',
        name=object_subtype_enum.NEWS_PAGE,
        template='news_list.html',
        icon='bi-file-earmark-easel',
        properties=[],
    ),
    PageTypeModel(
        label='Faq List',
        name=object_subtype_enum.FAQ_PAGE,
        template='faq_list.html',
        icon='bi-file-earmark-text',
        properties=[],
    ),
    PageTypeModel(
        label='Calendar',
        name=object_subtype_enum.CALENDAR_PAGE,
        template='calendar.html',
        icon='bi-calendar',
        properties=[],
    ),
    PageTypeModel(
        label='Search',
        name=object_subtype_enum.SEARCH_PAGE,
        template='search.html',
        icon='bi-search',
        properties=[],
    ),
    PageTypeModel(
        label='Login',
        name=object_subtype_enum.LOGIN_PAGE,
        template='login.html',
        icon='bi-key',
        properties=[],
    ),
    PageTypeModel(
        label='Contact',
        name=object_subtype_enum.CONTACT_PAGE,
        template='contact.html',
        icon='bi-file-earmark-person',
        properties=[],
    ),
    PageTypeModel(
        label='Sitemap',
        name=object_subtype_enum.SITEMAP_PAGE,
        template='sitemap.html',
        icon='bi-map',
        properties=[],
    ),
    PageTypeModel(
        label='Blog',
        name=object_subtype_enum.BLOG_PAGE,
        template='blog.html',
        icon='bi-postage',
        properties=[],
    ),
    # Add more...
]

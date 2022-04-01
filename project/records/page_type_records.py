"""
Context records module.
"""
from project.models.page_type_model import PageTypeModel


page_type_records: list[PageTypeModel] = [
    PageTypeModel(
        label='Article List',
        name='article_list',
        template='article_list.html',
        icon='bi-file-earmark-post',
        properties=[],
    ),
    PageTypeModel(
        label='Event List',
        name='event_list',
        template='event_list.html',
        icon='bi-file-earmark-medical',
        properties=[],
    ),
    PageTypeModel(
        label='News List',
        name='news_list',
        template='news_list.html',
        icon='bi-file-earmark-easel',
        properties=[],
    ),
    PageTypeModel(
        label='Faq List',
        name='faq_list',
        template='faq_list.html',
        icon='bi-file-earmark-text',
        properties=[],
    ),
    PageTypeModel(
        label='Calendar',
        name='calendar',
        template='calendar.html',
        icon='bi-calendar',
        properties=[],
    ),
    PageTypeModel(
        label='Search',
        name='search',
        template='search.html',
        icon='bi-search',
        properties=[],
    ),
    PageTypeModel(
        label='Login',
        name='login',
        template='login.html',
        icon='bi-key',
        properties=[],
    ),
    PageTypeModel(
        label='Contact',
        name='contact',
        template='contact.html',
        icon='bi-file-earmark-person',
        properties=[],
    ),
    PageTypeModel(
        label='Sitemap',
        name='sitemap',
        template='sitemap.html',
        icon='bi-map',
        properties=[],
    ),
    PageTypeModel(
        label='Blog',
        name='blog',
        template='blog.html',
        icon='bi-postage',
        properties=[],
    ),
    # Add more...
]

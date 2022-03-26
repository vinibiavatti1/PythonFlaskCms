"""
Context records module.
"""
from project.models.page_model import PageModel


page_records: list[PageModel] = [
    PageModel(
        name='article_list',
    ),
    PageModel(
        name='event_list',
    ),
    PageModel(
        name='news_list',
    ),
    PageModel(
        name='faq_list',
    ),
    PageModel(
        name='calendar',
    ),
    PageModel(
        name='search',
    ),
    PageModel(
        name='login',
    ),
    PageModel(
        name='contact',
    ),
    PageModel(
        name='sitemap',
    ),
    PageModel(
        name='blog',
    ),
    # Add more...
]

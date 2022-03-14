"""
Special URLs records module.
"""
from project.models.special_url_model import SpecialUrlModel


special_urls: list[SpecialUrlModel] = [
    SpecialUrlModel(
        url='/<lang>/login',
        sitemap_priority=0.0,
        sitemap_change_frequently='never',
        sitemap_active=True,
    ),
    SpecialUrlModel(
        url='/<lang>/blog',
        sitemap_priority=0.5,
        sitemap_change_frequently='always',
        sitemap_active=True,
    ),
    SpecialUrlModel(
        url='/<lang>/faq',
        sitemap_priority=0.5,
        sitemap_change_frequently='always',
        sitemap_active=True,
    ),
    # Add more...
]

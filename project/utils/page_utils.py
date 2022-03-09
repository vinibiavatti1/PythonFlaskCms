"""
Page utilities module.
"""
from project.services import property_service


def generate_title(page_title: str) -> str:
    """
    Generate title buy property template.
    """
    title = property_service.get_property('seo_title_template')
    website_title = property_service.get_property('website_title')
    if not title:
        return page_title
    if not page_title:
        page_title = property_service.get_property('seo_default_title')
    title = title.replace('{{WEBSITE_TITLE}}', website_title)
    title = title.replace('{{PAGE_TITLE}}', page_title)
    return title

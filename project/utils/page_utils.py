"""
Page utilities module.
"""
from project.services import property_service
from project.utils import context_utils


def generate_title(page_title: str) -> str:
    """
    Generate title buy property template.
    """
    context = context_utils.get_current_context()
    if not context:
        return page_title
    title = property_service.get_property_value(
        context,
        'seo_title_template'
    )
    website_title = property_service.get_property_value(
        context,
        'website_title'
    )
    if not title:
        return page_title
    if not page_title:
        page_title = property_service.get_property_value(
            context,
            'seo_default_title'
        )
    title = title.replace('{{WEBSITE_TITLE}}', website_title)
    title = title.replace('{{PAGE_TITLE}}', page_title)
    return title

"""
Sitemap service module.

This module provides features as business rules for sitemap.
"""
from typing import Any
from project.repositories import page_repository
from project.services import page_service


def select_page_urls() -> list[Any]:
    """
    Return all active page urls.
    """
    pages = [{**p} for p in page_repository.select_all(True)]
    for page in pages:
        page['url'] = page_service.generate_page_url(
            page['idiom'],
            page['name'],
        )
    return pages

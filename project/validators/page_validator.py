"""
Page Validator.

This module provides validator for page data.
"""
from typing import Any
from project.utils import validation_utils


def validate_save_data(form_data: dict[str, Any]) -> None:
    """
    Validate page insert data.
    """
    validation_utils.validate_form_data_fields(
        form_data,
        'name',
        'idiom',
        'title',
        'author',
        'description',
        'keywords',
        'canonical_urls',
        'sitemap_active',
        'sitemap_priority',
        'sitemap_change_frequently',
        'template',
        'html',
        'css',
        'script',
        'json',
        'properties',
        'access',
        'inject_posts',
        'inject_faqs',
        'inject_events',
    )
    validation_utils.validate_name(str(form_data.get('name')))

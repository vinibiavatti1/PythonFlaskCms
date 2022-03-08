"""
Page Validator.

This module provides validator for page data.
"""
from typing import Any
from project.errors import ValidationError
import re


def validate_insert_data(form_data: dict[str, Any]) -> None:
    """
    Validate page insert data.
    """
    if 'name' not in form_data:
        raise ValidationError('Name is required')
    if 'idiom' not in form_data:
        raise ValidationError('Idiom is required')
    if 'layout' not in form_data:
        raise ValidationError('Layout is required')
    if 'created_by' not in form_data:
        raise ValidationError('Created_By is required')
    if 'updated_by' not in form_data:
        raise ValidationError('Updated_By is required')
    if 'title' not in form_data:
        raise ValidationError('Title is required')
    if 'author' not in form_data:
        raise ValidationError('Author is required')
    if 'description' not in form_data:
        raise ValidationError('Description is required')
    if 'keywords' not in form_data:
        raise ValidationError('Keywords is required')
    if 'canonical_urls' not in form_data:
        raise ValidationError('Canonical_Urls is required')
    if 'sitemap_active' not in form_data:
        raise ValidationError('Sitemap_Active is required')
    if 'sitemap_priority' not in form_data:
        raise ValidationError('Sitemap_Priority is required')
    if 'sitemap_change_frequently' not in form_data:
        raise ValidationError('Sitemap_Change_Frequently is required')
    if 'template' not in form_data:
        raise ValidationError('Template is required')
    if 'html' not in form_data:
        raise ValidationError('Html is required')
    if 'properties' not in form_data:
        raise ValidationError('Properties is required')
    if 'json' not in form_data:
        raise ValidationError('JSON is required')
    if not re.match(r'^[a-z_]+$', form_data.get('name')):  # type: ignore
        raise ValidationError(
            'The name can contains only low characters and "_" as separator'
        )


def validate_update_data(form_data: dict[str, Any]) -> None:
    """
    Validate page update data.
    """
    if 'idiom' not in form_data:
        raise ValidationError('Idiom is required')
    if 'layout' not in form_data:
        raise ValidationError('Layout is required')
    if 'updated_by' not in form_data:
        raise ValidationError('Updated_By is required')
    if 'updated_on' not in form_data:
        raise ValidationError('Updated_On is required')
    if 'title' not in form_data:
        raise ValidationError('Title is required')
    if 'author' not in form_data:
        raise ValidationError('Author is required')
    if 'description' not in form_data:
        raise ValidationError('Description is required')
    if 'keywords' not in form_data:
        raise ValidationError('Keywords is required')
    if 'canonical_urls' not in form_data:
        raise ValidationError('Canonical_Urls is required')
    if 'sitemap_active' not in form_data:
        raise ValidationError('Sitemap_Active is required')
    if 'sitemap_priority' not in form_data:
        raise ValidationError('Sitemap_Priority is required')
    if 'sitemap_change_frequently' not in form_data:
        raise ValidationError('Sitemap_Change_Frequently is required')
    if 'template' not in form_data:
        raise ValidationError('Template is required')
    if 'html' not in form_data:
        raise ValidationError('Html is required')
    if 'properties' not in form_data:
        raise ValidationError('Properties is required')
    if 'json' not in form_data:
        raise ValidationError('JSON is required')

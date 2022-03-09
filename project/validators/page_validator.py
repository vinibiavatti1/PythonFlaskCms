"""
Page Validator.

This module provides validator for page data.
"""
from typing import Any
from project.errors import ValidationError
from project.utils.validation_utils import validate_form_data_fields
import re


def validate_insert_data(form_data: dict[str, Any]) -> None:
    """
    Validate page insert data.
    """
    validate_form_data_fields(
        form_data,
        'name',
        'idiom',
        'layout',
        'created_by',
        'updated_by',
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
        'id_menu',
    )
    if not re.match(r'^[a-z_]+$', str(form_data.get('name'))):
        raise ValidationError(
            'The name supports low characters and "_" as separator only'
        )


def validate_update_data(form_data: dict[str, Any]) -> None:
    """
    Validate page update data.
    """
    validate_form_data_fields(
        form_data,
        'name',
        'idiom',
        'layout',
        'updated_on',
        'updated_by',
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
        'id_menu',
    )
    if not re.match(r'^[a-z_]+$', str(form_data.get('name'))):
        raise ValidationError(
            'The name supports low characters and "_" as separator only'
        )

"""
Page service module.

This module provides features as business rules for pages.
"""
from typing import Any, Optional
from project.validators import page_validator
from project.repositories import page_repository
from project.services import history_service
from project.enums import resource_type_enum
from flask import session
from project.enums import session_enum
from datetime import datetime


def insert(data: dict[str, Any]) -> int:
    """
    Validate and insert page data to database.

    Return it's id after insert.
    """
    data['properties'] = '{}'
    page_validator.validate_insert_data(data)
    new_id = page_repository.insert(data)
    history_service.insert(
        new_id,
        resource_type_enum.PAGE,
        'Page created'
    )
    return new_id


def update(page_id: int, data: dict[str, Any]) -> None:
    """
    Validate and update page data to database.
    """
    data['properties'] = '{}'
    page_validator.validate_update_data(data)
    page_repository.update(page_id, data)
    history_service.insert(
        page_id,
        resource_type_enum.PAGE,
        'Page updated'
    )


def select_all(active: Optional[bool] = None) -> list[Any]:
    """
    Return all pages.
    """
    return page_repository.select_all(active)


def select_by_id(page_id: int) -> Optional[dict[str, Any]]:
    """
    Get page by id.
    """
    return page_repository.select(page_id)


def generate_page_url(idiom: str, page_name: str) -> str:
    """
    Generate the page URL.
    """
    return f'/page/{idiom}/{page_name}'


def delete(page_id: int) -> None:
    """
    Delete page by id.
    """
    page_repository.delete(page_id)
    history_service.insert(
        page_id,
        resource_type_enum.PAGE,
        'Page deleted'
    )


def duplicate(page_id: int, name: str) -> int:
    """
    Duplicate page by id with new name.
    """
    page = page_repository.select(page_id)
    if page is None:
        raise ValueError(f'Page {page_id} was not found')
    page_dict = {**page}
    page_dict['name'] = name
    new_id = page_repository.insert(page_dict)
    history_service.insert(
        page_id,
        resource_type_enum.PAGE,
        'Page duplicated'
    )
    history_service.insert(
        new_id,
        resource_type_enum.PAGE,
        'Page created'
    )
    return new_id

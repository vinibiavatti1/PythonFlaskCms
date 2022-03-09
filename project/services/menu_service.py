"""
Menu service module.

This module provides features as business rules for menus.
"""
from typing import Any, Optional
from project.validators import menu_validator
from project.repositories import menu_repository
from flask import session
from project.enums import session_enum
from datetime import datetime


def insert(data: dict[str, Any]) -> int:
    """
    Validate and insert menu data to database.

    Return it's id after insert.
    """
    user_id = session[session_enum.USER_ID]
    data['created_by'] = user_id
    data['updated_by'] = user_id
    data['properties'] = '{}'
    menu_validator.validate_insert_data(data)
    return menu_repository.insert(data)


def update(id_: int, data: dict[str, Any]) -> None:
    """
    Validate and update menu data to database.
    """
    user_id = session[session_enum.USER_ID]
    data['updated_by'] = user_id
    data['updated_on'] = datetime.now()
    data['properties'] = '{}'
    menu_validator.validate_update_data(data)
    menu_repository.update(id_, data)


def select_all(active: Optional[bool] = None) -> list[Any]:
    """
    Return all menus.
    """
    return menu_repository.select_all(active)


def select_by_id(menu_id: int) -> Optional[dict[str, Any]]:
    """
    Get menu by id.
    """
    return menu_repository.select(menu_id)


def delete(menu_id: int) -> None:
    """
    Delete menu by id.
    """
    menu_repository.delete(menu_id)

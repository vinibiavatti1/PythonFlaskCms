"""
Menu service module.

This module provides features as business rules for menus.
"""
from typing import Any, Optional
from project.validators import menu_validator
from project.repositories import menu_repository
from flask import session
from project.enums import session_enum
from project.services import history_service
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
    new_id = menu_repository.insert(data)
    history_service.insert(new_id, 'menu', 'Menu created')
    return new_id


def update(menu_id: int, data: dict[str, Any]) -> None:
    """
    Validate and update menu data to database.
    """
    user_id = session[session_enum.USER_ID]
    data['updated_by'] = user_id
    data['updated_on'] = datetime.now()
    data['properties'] = '{}'
    menu_validator.validate_update_data(data)
    menu_repository.update(menu_id, data)
    history_service.insert(menu_id, 'menu', 'Menu updated')


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
    history_service.insert(menu_id, 'menu', 'Menu deleted')


def duplicate(menu_id: int, name: str) -> int:
    """
    Duplicate menu by id with new name.
    """
    user_id = session[session_enum.USER_ID]
    page = menu_repository.select(menu_id)
    if page is None:
        raise ValueError(f'Menu {menu_id} was not found')
    menu_dict = {**page}
    menu_dict['name'] = name
    menu_dict['created_by'] = user_id
    menu_dict['updated_by'] = user_id
    menu_dict['created_on'] = datetime.now()
    menu_dict['updated_on'] = datetime.now()
    history_service.insert(menu_id, 'menu', 'Menu duplicated')
    new_id = menu_repository.insert(menu_dict)
    history_service.insert(new_id, 'menu', 'Menu created')
    return new_id

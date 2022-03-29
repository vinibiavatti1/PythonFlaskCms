"""
Translation functions module.
"""
from typing import Any
from flask import session
from project.repositories import translation_repository
from project.enums import resource_type_enum, session_enum
from project.services import history_service


def select_all(context: str) -> Any:
    """
    Select all translations.
    """
    return translation_repository.select_all(context)


def select_by_id(translation_id: int) -> Any:
    """
    Select translation by id.
    """
    return translation_repository.select_by_id(translation_id)


def select_by_name(context: str, name: str) -> Any:
    """
    Select translation by context and name.
    """
    return translation_repository.select_by_name(context, name)


def insert(context: str, data: dict[str, Any]) -> Any:
    """
    Insert new translation.
    """
    new_id = translation_repository.insert(context, data)
    history_service.insert(
        new_id,
        resource_type_enum.TRANSLATION,
        'Translaton created'
    )
    return new_id


def update(translation_id: int, data: dict[str, Any]) -> Any:
    """
    Update translation.
    """
    translation_repository.update(translation_id, data)
    history_service.insert(
        translation_id,
        resource_type_enum.TRANSLATION,
        'Translaton updated'
    )
    return translation_id


def delete(translation_id: int) -> Any:
    """
    Delete translation.
    """
    translation_repository.delete(translation_id)
    history_service.insert(
        translation_id,
        resource_type_enum.TRANSLATION,
        'Translaton deleted'
    )
    return translation_id

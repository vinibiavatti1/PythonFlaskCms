"""
Translation functions module.
"""
from typing import Any
from flask import session
from project.repositories import translation_repository
from project.enums import resource_type_enum, session_enum
from project.services import history_service


def select_all() -> Any:
    """
    Select all translations.
    """
    context = session[session_enum.CONTEXT]
    return translation_repository.select_all(context)


def select_by_id(translation_id: int) -> Any:
    """
    Select translation by id.
    """
    context = session[session_enum.CONTEXT]
    return translation_repository.select_by_id(context, translation_id)


def select_by_name(name: str) -> Any:
    """
    Select translation by name.
    """
    context = session[session_enum.CONTEXT]
    return translation_repository.select_by_idiom_and_name(context, name)


def insert(data: dict[str, Any]) -> Any:
    """
    Insert new translation.
    """
    context = session[session_enum.CONTEXT]  # REPENSAR
    new_id = translation_repository.insert(data)
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

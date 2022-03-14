"""
Translation functions module.
"""
from typing import Any
from project.repositories import translation_repository
from project.enums import resource_type_enum
from project.services import history_service


def select_all() -> Any:
    """
    Select all translations.
    """
    return translation_repository.select_all()


def select_by_id(translation_id: int) -> Any:
    """
    Select translation by id.
    """
    return translation_repository.select_by_id(translation_id)


def insert(data: dict[str, Any]) -> Any:
    """
    Insert new translation.
    """
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

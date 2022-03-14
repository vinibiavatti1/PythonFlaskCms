"""
Redirect functions module.
"""
from typing import Any
from project.repositories import redirect_repository
from project.enums import resource_type_enum
from project.services import history_service


def select_all() -> Any:
    """
    Select all redirects.
    """
    return redirect_repository.select_all()


def select_by_id(redirect_id: int) -> Any:
    """
    Select redirect by id.
    """
    return redirect_repository.select_by_id(redirect_id)


def insert(data: dict[str, Any]) -> Any:
    """
    Insert new redirect.
    """
    new_id = redirect_repository.insert(data)
    history_service.insert(
        new_id,
        resource_type_enum.REDIRECT,
        'Redirect created'
    )
    return new_id


def update(redirect_id: int, data: dict[str, Any]) -> Any:
    """
    Update redirect.
    """
    redirect_repository.update(redirect_id, data)
    history_service.insert(
        redirect_id,
        resource_type_enum.REDIRECT,
        'Redirect updated'
    )
    return redirect_id


def delete(redirect_id: int) -> Any:
    """
    Delete redirect.
    """
    redirect_repository.delete(redirect_id)
    history_service.insert(
        redirect_id,
        resource_type_enum.REDIRECT,
        'Redirect deleted'
    )
    return redirect_id

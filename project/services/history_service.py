"""
History functions module.
"""
from flask import session
from project.enums import session_enum
from typing import Any
from project.repositories import history_repository


def insert(context: str, resource_id: int, resource_type: str,
           description: str) -> None:
    """
    Insert new history.
    """
    user_id = session[session_enum.USER_ID]
    data = dict(
        resource_id=resource_id,
        resource_type=resource_type,
        description=description,
        created_by=user_id
    )
    history_repository.insert(context, data)


def select_by_resource(context: str, resource_id: int,
                       resource_type: str) -> list[dict[str, Any]]:
    """
    Select the history by resource id and type.
    """
    return history_repository.select_by_resource(
        context,
        resource_id,
        resource_type
    )

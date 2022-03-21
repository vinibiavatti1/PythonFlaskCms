"""
Content service.
"""
from flask import session
from calendar import c
from typing import Any, Optional
from project.enums import session_enum
from project.repositories import content_repository
from project.services import history_service
from project.utils import data_utils
import json


def select_all(context: str, content_type: str) -> list[dict[str, Any]]:
    """
    Select all contents by content type.
    """
    contents = content_repository.select_all(context, content_type)
    return data_utils.parse_list_json_data(contents)


def select_all_deleted(context: str) -> list[dict[str, Any]]:
    """
    Select all deleted contents.
    """
    contents = content_repository.select_all_deleted(context)
    return data_utils.parse_list_json_data(contents)


def select_by_id(context: str, content_id: int) -> Optional[dict[str, Any]]:
    """
    Select a content by id.
    """
    content = content_repository.select_by_id(context, content_id)
    if not content:
        return None
    return data_utils.parse_json_data(content)


def insert(context: str, data: dict[str, Any]) -> Any:
    """
    Insert a new content to database.
    """
    data['url'] = generate_content_url(
        context,
        data['type'],
        data['name'],
    )
    data['data'] = json.dumps(data)
    content_id = content_repository.insert(context, data)
    history_service.insert(
        content_id,
        'Content created'
    )
    return content_id


def update(context: str, content_id: int, data: dict[str, Any]) -> Any:
    """
    Update a content by id.
    """
    data['url'] = generate_content_url(
        context,
        data['type'],
        data['name'],
    )
    data['data'] = json.dumps(data)
    content_id = content_repository.update(context, content_id, data)
    history_service.insert(
        content_id,
        'Content updated'
    )


def delete(context: str, content_id: int) -> None:
    """
    Delete a content by id.
    """
    content = content_repository.select_by_id(context, content_id)
    if not content:
        return
    content_repository.delete(context, content_id)
    history_service.insert(
        content_id,
        'Content deleted'
    )


def restore(context: str, content_id: int) -> None:
    """
    Restore a content by id.
    """
    content_repository.restore(context, content_id)
    history_service.insert(
        content_id,
        'Content restored'
    )


def duplicate(context: str, content_id: int, to_context: str) -> Any:
    """
    Delete a content by id.
    """
    content = content_repository.select_by_id(context, content_id)
    if not content:
        return
    content_dict = {
        **content
    }
    content_dict['published'] = 0
    new_id = content_repository.insert(to_context, content_dict)
    history_service.insert(
        content_id,
        f'Content duplicated (id={new_id})',
    )
    return new_id


def generate_content_url(context: str, content_type: str,
                         content_name: str) -> str:
    """
    Generate the content URL.
    """
    return f'/{context}/{content_type}/{content_name}'

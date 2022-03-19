"""
Content service.
"""
from calendar import c
from typing import Any, Optional
from project.repositories import content_repository
from project.services import history_service
from project.utils import data_utils
import json


def select_all(idiom: str, content_type: str) -> list[dict[str, Any]]:
    """
    Select all contents by content type.
    """
    contents = content_repository.select_all(idiom, content_type)
    return data_utils.parse_list_json_data(contents)


def select_all_deleted(idiom: str) -> list[dict[str, Any]]:
    """
    Select all deleted contents.
    """
    contents = content_repository.select_all_deleted(idiom)
    return data_utils.parse_list_json_data(contents)


def select_by_id(content_id: int) -> Optional[dict[str, Any]]:
    """
    Select a content by id.
    """
    content = content_repository.select_by_id(content_id)
    if not content:
        return None
    return data_utils.parse_json_data(content)


def insert(data: dict[str, Any]) -> Any:
    """
    Insert a new content to database.
    """
    data['idiom'] = 'en'  # TODO
    data['url'] = generate_content_url(
        'en',
        data['type'],
        data['name'],
    )
    data['data'] = json.dumps(data)
    content_id = content_repository.insert(data)
    history_service.insert(content_id, data['type'], 'Content created')
    return content_id


def update(content_id: int, data: dict[str, Any]) -> Any:
    """
    Update a content by id.
    """
    data['idiom'] = 'en'  # TODO
    data['url'] = generate_content_url(
        'en',
        data['type'],
        data['name'],
    )
    data['data'] = json.dumps(data)
    content_id = content_repository.update(content_id, data)
    history_service.insert(content_id, data['type'], 'Content updated')


def delete(content_id: int) -> None:
    """
    Delete a content by id.
    """
    content_repository.delete(content_id)


def duplicate(content_id: int, idiom: str) -> Any:
    """
    Delete a content by id.
    """
    content = content_repository.select_by_id(content_id)
    if not content:
        return
    content_dict = {
        **content
    }
    content_dict['idiom'] = idiom
    new_id = content_repository.insert(content_dict)
    history_service.insert(
        content_id,
        content['type'],
        f'Content duplicated (id={new_id})',
    )
    return new_id


def generate_content_url(idiom: str, content_type: str,
                         content_name: str) -> str:
    """
    Generate the content URL.
    """
    return f'/{idiom}/{content_type}/{content_name}'

"""
Content repository.
"""
from typing import Any, Optional
from project.utils import database_utils
from project.entities.content_entity import ContentEntity
import json


def select_all_by_type(context: str,
                       resource_type: str) -> list[ContentEntity]:
    """
    Select all contents by content type.
    """
    sql = '''
        SELECT * FROM contents
        WHERE resource_type = ? AND context = ? AND deleted = 0
    '''
    result_set = database_utils.execute_query(sql, (resource_type, context))
    return ContentEntity.map_list_to_entity(result_set)


def select_all(context: str) -> list[ContentEntity]:
    """
    Select all contents.
    """
    sql = '''
        SELECT * FROM contents
        WHERE deleted = 0 AND context = ?

    '''
    result_set = database_utils.execute_query(sql, (context,))
    return ContentEntity.map_list_to_entity(result_set)


def select_by_name(context: str, name: str) -> Optional[ContentEntity]:
    """
    Select all contents by name.
    """
    sql = '''
        SELECT * FROM contents
        WHERE deleted = 0 AND context = ? AND name = ?

    '''
    result_set = database_utils.execute_single_query(sql, (context, name))
    if result_set is None:
        return None
    return ContentEntity.map_dict_to_entity(result_set)


def select_all_deleted(context: str) -> list[ContentEntity]:
    """
    Select all deleted contents.
    """
    sql = '''
        SELECT * FROM contents
        WHERE deleted = 1 AND context = ?
    '''
    result_set = database_utils.execute_query(sql, (context,))
    return ContentEntity.map_list_to_entity(result_set)


def select_by_id(content_id: int) -> Optional[ContentEntity]:
    """
    Select a content by id.
    """
    sql = '''
        SELECT * FROM contents
        WHERE deleted = 0 AND id = ?
    '''
    result_set = database_utils.execute_single_query(sql, (content_id,))
    if result_set is None:
        return None
    return ContentEntity.map_dict_to_entity(result_set)


def insert(content: ContentEntity) -> Any:
    """
    Insert a new content to database.
    """
    sql = '''
        INSERT INTO contents (context, name, resource_type, data)
        VALUES (?, ?, ?, ?)
    '''
    return database_utils.execute_update(sql, (
        content.context,
        content.name,
        content.resource_type,
        json.dumps(content.data),
    ))


def update(content: ContentEntity) -> Any:
    """
    Update a content by id.
    """
    sql = '''
        UPDATE contents
        SET context = ?, name = ?, resource_type = ?, data = ?
        WHERE id = ?
    '''
    database_utils.execute_update(sql, (
        content.context,
        content.name,
        content.resource_type,
        json.dumps(content.data),
        content.id
    ))
    return content.id


def delete(content_id: int) -> Any:
    """
    Delete a content by id.
    """
    sql = '''
        UPDATE contents
        SET deleted = 1, deleted_on = CURRENT_TIMESTAMP
        WHERE id = ?
    '''
    database_utils.execute_update(sql, (content_id,))
    return content_id


def restore(content_id: int) -> Any:
    """
    Restore a content by id.
    """
    sql = '''
        UPDATE contents
        SET deleted = 0, deleted_on = NULL
        WHERE id = ?
    '''
    database_utils.execute_update(sql, (content_id,))
    return content_id

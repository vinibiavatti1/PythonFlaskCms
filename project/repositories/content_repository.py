"""
Content repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def select_all(idiom: str, content_type: str) -> list[dict[str, Any]]:
    """
    Select all contents by content type.
    """
    sql = '''
        SELECT * FROM contents WHERE deleted = 0 AND type = ? AND idiom = ?
    '''
    return database_utils.execute_query(sql, (content_type, idiom))


def select_all_deleted(idiom: str) -> list[dict[str, Any]]:
    """
    Select all deleted contents.
    """
    sql = '''
        SELECT * FROM contents WHERE deleted = 1 AND idiom = ?
    '''
    return database_utils.execute_query(sql, (idiom,))


def select_by_id(content_id: int) -> Optional[dict[str, Any]]:
    """
    Select a content by id.
    """
    sql = '''
        SELECT * FROM contents WHERE deleted = 0 AND id = ?
    '''
    return database_utils.execute_single_query(sql, (content_id,))


def insert(data: dict[str, Any]) -> Any:
    """
    Insert a new content to database.
    """
    sql = '''
        INSERT INTO contents
        (idiom, name, type, published, data)
        VALUES
        (?, ?, ?, ?, ?)
    '''
    return database_utils.execute_update(sql, (
        data['idiom'],
        data['name'],
        data['type'],
        data['published'],
        data['data'],
    ))


def update(content_id: int, data: dict[str, Any]) -> Any:
    """
    Update a content by id.
    """
    sql = '''
        UPDATE contents SET
            idiom = ?,
            name = ?,
            type = ?,
            published = ?,
            data = ?
        WHERE id = ?
    '''
    return database_utils.execute_update(sql, (
        data['idiom'],
        data['name'],
        data['type'],
        data['published'],
        data['data'],
        content_id
    ))


def delete(content_id: int) -> None:
    """
    Delete a content by id.
    """
    sql = '''
        UPDATE contents SET deleted = 1 WHERE id = ?
    '''
    database_utils.execute_update(sql, (content_id))

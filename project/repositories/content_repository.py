"""
Content repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def select_all(context: str, content_type: str) -> list[dict[str, Any]]:
    """
    Select all contents by content type.
    """
    sql = '''
        SELECT * FROM contents WHERE deleted = 0 AND type = ? AND context = ?
    '''
    return database_utils.execute_query(sql, (content_type, context))


def select_all_deleted(context: str) -> list[dict[str, Any]]:
    """
    Select all deleted contents.
    """
    sql = '''
        SELECT * FROM contents WHERE deleted = 1 AND context = ?
    '''
    return database_utils.execute_query(sql, (context,))


def select_by_id(context: str, content_id: int) -> Optional[dict[str, Any]]:
    """
    Select a content by id.
    """
    sql = '''
        SELECT * FROM contents WHERE deleted = 0 AND id = ? AND context = ?
    '''
    return database_utils.execute_single_query(sql, (content_id, context))


def insert(context: str, data: dict[str, Any]) -> Any:
    """
    Insert a new content to database.
    """
    sql = '''
        INSERT INTO contents
        (context, name, type, published, data)
        VALUES
        (?, ?, ?, ?, ?)
    '''
    return database_utils.execute_update(sql, (
        context,
        data['name'],
        data['type'],
        data['published'],
        data['data'],
    ))


def update(context: str, content_id: int, data: dict[str, Any]) -> Any:
    """
    Update a content by id.
    """
    sql = '''
        UPDATE contents SET
            context = ?,
            name = ?,
            type = ?,
            published = ?,
            data = ?
        WHERE id = ?
    '''
    return database_utils.execute_update(sql, (
        context,
        data['name'],
        data['type'],
        data['published'],
        data['data'],
        content_id
    ))


def delete(context: str, content_id: int) -> None:
    """
    Delete a content by id.
    """
    sql = '''
        UPDATE contents SET deleted = 1,
        deleted_on = CURRENT_TIMESTAMP
        WHERE id = ? AND context = ?
    '''
    database_utils.execute_update(sql, (content_id, context))


def restore(context: str, content_id: int) -> None:
    """
    Restore a content by id.
    """
    sql = '''
        UPDATE contents SET deleted = 0,
        deleted_on = NULL
        WHERE id = ? AND context = ?
    '''
    database_utils.execute_update(sql, (content_id, context))

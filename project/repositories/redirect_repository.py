"""
Redirect repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def insert(data: dict[str, Any]) -> Any:
    """
    Insert redirect.
    """
    sql = '''
        INSERT INTO redirects (
            from_url,
            to_url
        ) VALUES (?, ?)
    '''
    return database_utils.execute_update(sql, (
        data['from_url'],
        data['to_url'],
    ))


def update(redirect_id: int, data: dict[str, Any]) -> Any:
    """
    Update redirect.
    """
    sql = '''
        UPDATE redirects SET
            from_url = ?,
            to_url = ?
        WHERE
            id = ?
    '''
    return database_utils.execute_update(sql, (
        data['from_url'],
        data['to_url'],
        redirect_id,
    ))


def select_all() -> list[dict[str, Any]]:
    """
    Get all redirect records.
    """
    sql = '''
        SELECT * FROM redirects
        WHERE deleted = 0 ORDER BY id
    '''
    return database_utils.execute_query(sql)


def select_by_id(redirect_id: int) -> Optional[dict[str, Any]]:
    """
    Get redirect by id.
    """
    sql = '''
        SELECT * FROM redirects
        WHERE id = ? AND deleted = 0
    '''
    return database_utils.execute_single_query(sql, (redirect_id,))


def delete(redirect_id: int) -> list[dict[str, Any]]:
    """
    Delete redirect.
    """
    sql = '''
        UPDATE redirects SET deleted = 1
        WHERE id = ?
    '''
    return database_utils.execute_query(sql, (redirect_id,))

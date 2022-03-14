"""
Block repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def insert(page_id: int, block_name: str, data: str) -> Any:
    """
    Insert block to page.
    """
    sql = '''
        INSERT INTO blocks (
            id_page,
            name,
            json
        ) VALUES (?, ?, ?)
    '''
    return database_utils.execute_update(sql, (
        page_id,
        block_name,
        data,
    ))


def update(block_id: int, data: str) -> Any:
    """
    Update translation.
    """
    sql = '''
        UPDATE blocks SET
            json = ?
        WHERE
            id = ?
    '''
    return database_utils.execute_update(sql, (
        data,
        block_id,
    ))


def select_all(page_id: int) -> list[dict[str, Any]]:
    """
    Get all block of page.
    """
    sql = '''
        SELECT * FROM blocks
        WHERE deleted = 0 AND id_page = ? ORDER BY id
    '''
    return database_utils.execute_query(sql, (page_id,))


def select_by_id(block_id: int) -> Optional[dict[str, Any]]:
    """
    Get block by id.
    """
    sql = '''
        SELECT * FROM blocks
        WHERE id = ? AND deleted = 0
    '''
    return database_utils.execute_single_query(sql, (block_id,))


def delete(block_id: int) -> list[dict[str, Any]]:
    """
    Delete block.
    """
    sql = '''
        UPDATE blocks SET deleted = 1
        WHERE id = ?
    '''
    return database_utils.execute_query(sql, (block_id,))

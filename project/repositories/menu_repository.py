"""
Menu SQLite repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def select_all(active: Optional[bool] = None) -> list[Any]:
    """
    List menus.
    """
    sql = '''
        SELECT * FROM menus
        WHERE deleted = 0
    '''
    if active is not None:
        sql += ' AND menu.active = ' + ('1' if active else '0')
    return database_utils.execute_query(sql)


def select(menu_id: int) -> Optional[Any]:
    """
    List menus.
    """
    sql = '''
        SELECT * FROM menus
        WHERE id = ? AND deleted = 0
    '''
    return database_utils.execute_single_query(sql, menu_id)


def insert(data: dict[str, Any]) -> int:
    """
    Insert menu to database and return the ID.
    """
    sql = '''
        INSERT INTO menus (
            name,
            json,
            idiom)
        VALUES
            (?, ?, ?, ?)
    '''
    menu_id = database_utils.execute_update(
        sql,
        (
            data['name'],
            data['json'],
            data['idiom'],
        )
    )
    return int(menu_id)


def update(menu_id: int, data: dict[str, Any]) -> None:
    """
    Update menu.
    """
    sql = '''
        UPDATE menus SET
            name = ?,
            json = ?,
            active = ?,
            idiom = ?
        WHERE
            id = ?
    '''
    database_utils.execute_update(
        sql,
        (
            data['name'],
            data['json'],
            data['active'],
            data['idiom'],
            menu_id,
        )
    )


def delete(menu_id: int) -> None:
    """
    Delete menu by id.
    """
    sql = 'UPDATE menus SET deleted = 1 WHERE id = ?'
    database_utils.execute_update(sql, (menu_id,))

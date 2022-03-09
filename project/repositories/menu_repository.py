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
        SELECT
            menu.id,
            menu.name,
            user.name as created_by_name,
            user2.name as updated_by_name,
            menu.created_on,
            menu.updated_on,
            menu.active
        FROM menus menu
        LEFT JOIN users user
        ON (menu.created_by == user.id)
        LEFT JOIN users user2
        ON (menu.updated_by == user2.id)
        WHERE menu.deleted = 0
    '''
    if active is not None:
        sql += ' AND menu.active = ' + ('1' if active else '0')
    return database_utils.execute_query(sql)


def select(menu_id: int) -> Optional[Any]:
    """
    List menus.
    """
    sql = '''
        SELECT
            menu.id,
            menu.name,
            menu.active,
            menu.created_by,
            menu.updated_by,
            menu.created_on,
            menu.updated_on,
            menu.json,
            user.name as created_by_name,
            user2.name as updated_by_name
        FROM menus menu
        LEFT JOIN users user
        ON (menu.created_by = user.id)
        LEFT JOIN users user2
        ON (menu.updated_by = user2.id)
        WHERE menu.id = ? AND menu.deleted = 0
    '''
    return database_utils.execute_single_query(sql, menu_id)


def insert(data: dict[str, Any]) -> int:
    """
    Insert menu to database and return the ID.
    """
    sql = '''
        INSERT INTO menus (
            name,
            created_by,
            updated_by,
            json)
        VALUES
            (?, ?, ?, ?)
    '''
    menu_id = database_utils.execute_update(
        sql,
        (
            data['name'],
            data['created_by'],
            data['updated_by'],
            data['json'],
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
            updated_by = ?,
            updated_on = CURRENT_TIMESTAMP,
            json = ?,
            active = ?
        WHERE
            id = ?
    '''
    database_utils.execute_update(
        sql,
        (
            data['name'],
            data['updated_by'],
            data['json'],
            data['active'],
            menu_id,
        )
    )


def delete(menu_id: int) -> None:
    """
    Delete menu by id.
    """
    sql = 'DELETE FROM menus WHERE id = ?'
    database_utils.execute_update(sql, (menu_id,))

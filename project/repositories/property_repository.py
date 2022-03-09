"""
Property repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def delete_property(name: str) -> None:
    """
    Delete property by name.
    """
    sql = 'DELETE FROM properties WHERE name = ?'
    database_utils.execute_update(sql, (name,))


def select_all() -> list[dict[str, Any]]:
    """
    Get all properties.
    """
    sql = 'SELECT * FROM properties'
    return database_utils.execute_query(sql)


def set_property(name: str, value: str) -> None:
    """
    Set property value.
    """
    delete_property(name)
    sql = 'INSERT INTO properties VALUES (?, ?)'
    database_utils.execute_update(sql, (name, value))


def get_property(name: str) -> Optional[Any]:
    """
    Get property value by name.
    """
    sql = 'SELECT * FROM properties WHERE name = ?'
    return database_utils.execute_single_query(sql, (name,))

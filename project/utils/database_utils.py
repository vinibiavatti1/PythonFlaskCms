"""
Database module.
"""
from project.config import config
from project.errors import AppError
from typing import Any, Optional, Union
import sqlite3
import sys
import os


CURRENT_DIR: str = sys.path[0]


def connect() -> sqlite3.Connection:
    """
    Connect to SQLite database and return the connection object.

    The connection data will be get from app configuration.
    """
    db_path = os.path.join(CURRENT_DIR, 'database', config['db_name'])
    connection = sqlite3.connect(db_path)
    if not connection:
        raise AppError('Could not connect to database')
    connection.row_factory = sqlite3.Row
    return connection


def execute_query(sql: str, data: Optional[Any] = None, *,
                  single: bool = False) -> Union[list[Any], Any]:
    """
    Execute SQLite DQL statement in database and return the resultset.
    """
    connection = connect()
    cursor = connection.cursor()
    if data:
        cursor.execute(sql, data)
    else:
        cursor.execute(sql)
    if single:
        return cursor.fetchone()
    else:
        return cursor.fetchall()


def execute_update(sql: str, data: Optional[Any] = None) -> Any:
    """
    Execute SQLite DDL statement in database and return the last inserted id.
    """
    connection = connect()
    cursor = connection.cursor()
    if data:
        cursor.execute(sql, data)
    else:
        cursor.execute(sql)
    connection.commit()
    return cursor.lastrowid

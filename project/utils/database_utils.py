"""
Database module.
"""
from project.errors import AppError
from typing import Any, Optional, Union
from project.enums import env_enum
import sqlite3
import sys
import os


CURRENT_DIR: str = sys.path[0]


def connect() -> sqlite3.Connection:
    """
    Connect to SQLite database and return the connection object.

    The connection data will be get from app configuration.
    """
    env = os.environ.get('FLASK_ENV')
    db_name = 'database_' + str(env) + '.db'
    db_path = os.path.join(CURRENT_DIR, 'database', db_name)
    connection = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    if not connection:
        raise AppError('Could not connect to database')
    connection.row_factory = sqlite3.Row
    return connection


def execute_query(sql: str, data: Optional[Any] = None) -> list[Any]:
    """
    Execute DQL statement in database and return the resultset as list.
    """
    connection = connect()
    cursor = connection.cursor()
    if data:
        cursor.execute(sql, data)
    else:
        cursor.execute(sql)
    return cursor.fetchall()


def execute_single_query(sql: str,
                         data: Optional[Any] = None) -> Optional[Any]:
    """
    Execute DQL statement in database and return the first result as dict.
    """
    connection = connect()
    cursor = connection.cursor()
    if data:
        cursor.execute(sql, data)
    else:
        cursor.execute(sql)
    return cursor.fetchone()


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

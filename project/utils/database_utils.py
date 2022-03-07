"""
Database module.
"""
from project.config import config
from project.errors import AppError
from typing import Any
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
    return connection


def execute(sql: str) -> list[Any]:
    """
    Execute SQLite query in database and return the resultset.
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

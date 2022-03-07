"""
Page SQLite repository.
"""
import sqlite3
from typing import Any


def list(type: str, active: bool = True) -> None:
    """
    List all landing pages.
    """
    pass


def save(_id: int, data: dict[str, Any]) -> None:
    """
    Test
    """
    sql = '''
        INSERT INTO pages
            (idiom, name, layout, created_by, updated_by, title, author,
            description, keywords, canonical_urls, sitemap_active,
            sitemap_priority, sitemap_change_frequently, template, html,
            properties)
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

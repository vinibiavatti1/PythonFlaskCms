"""
Page SQLite repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def select_all(active: Optional[bool] = None) -> list[Any]:
    """
    List pages.
    """
    sql = '''
        SELECT * FROM pages page
        WHERE deleted = 0
    '''
    if active is not None:
        sql += ' AND page.active = ' + ('1' if active else '0')
    return database_utils.execute_query(sql)


def select(page_id: int) -> Optional[Any]:
    """
    List pages.
    """
    sql = '''
        SELECT * FROM pages page
        WHERE id = ? AND deleted = 0
    '''
    return database_utils.execute_single_query(sql, page_id)


def insert(data: dict[str, Any]) -> int:
    """
    Insert page to database and return the ID.
    """
    sql = '''
        INSERT INTO pages (
            idiom,
            name,
            title,
            author,
            description,
            keywords,
            canonical_urls,
            sitemap_active,
            sitemap_priority,
            sitemap_change_frequently,
            template,
            html,
            css,
            script,
            json,
            properties,
            access)
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    page_id = database_utils.execute_update(
        sql,
        (
            data['idiom'],
            data['name'],
            data['title'],
            data['author'],
            data['description'],
            data['keywords'],
            data['canonical_urls'],
            data['sitemap_active'],
            data['sitemap_priority'],
            data['sitemap_change_frequently'],
            data['template'],
            data['html'],
            data['css'],
            data['script'],
            data['json'],
            data['properties'],
            data['access'],
        )
    )
    return int(page_id)


def update(page_id: int, data: dict[str, Any]) -> None:
    """
    Update page.
    """
    sql = '''
        UPDATE pages SET
            name = ?,
            idiom = ?,
            title = ?,
            author = ?,
            description = ?,
            keywords = ?,
            canonical_urls = ?,
            sitemap_active = ?,
            sitemap_priority = ?,
            sitemap_change_frequently = ?,
            template = ?,
            html = ?,
            css = ?,
            script = ?,
            json = ?,
            properties = ?,
            active = ?,
            access = ?
        WHERE
            id = ?
    '''
    database_utils.execute_update(
        sql,
        (
            data['name'],
            data['idiom'],
            data['title'],
            data['author'],
            data['description'],
            data['keywords'],
            data['canonical_urls'],
            data['sitemap_active'],
            data['sitemap_priority'],
            data['sitemap_change_frequently'],
            data['template'],
            data['html'],
            data['css'],
            data['script'],
            data['json'],
            data['properties'],
            data['active'],
            data['access'],
            page_id,
        )
    )


def delete(page_id: int) -> None:
    """
    Delete page by id.
    """
    sql = 'UPDATE pages SET deleted = 1 WHERE id = ?'
    database_utils.execute_update(sql, (page_id,))

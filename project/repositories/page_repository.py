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
        SELECT
            page.id,
            page.name,
            user.name as created_by_name,
            user2.name as updated_by_name,
            page.created_on,
            page.updated_on,
            page.active
        FROM pages page
        LEFT JOIN users user
        ON (page.created_by == user.id)
        LEFT JOIN users user2
        ON (page.updated_by == user2.id)
        WHERE page.deleted = 0
    '''
    if active is not None:
        sql += ' AND page.active = ' + ('1' if active else '0')
    return database_utils.execute_query(sql)


def select(page_id: int) -> Optional[dict[str, Any]]:
    """
    List pages.
    """
    sql = '''
        SELECT
            page.id,
            page.idiom,
            page.name,
            page.layout,
            page.template,
            page.active,
            page.created_by,
            page.updated_by,
            page.created_on,
            page.updated_on,
            page.title,
            page.author,
            page.description,
            page.keywords,
            page.canonical_urls,
            page.sitemap_active,
            page.sitemap_priority,
            page.sitemap_change_frequently,
            page.template,
            page.html,
            page.properties,
            page.json,
            user.name as created_by_name,
            user2.name as updated_by_name
        FROM pages page
        LEFT JOIN users user
        ON (page.created_by = user.id)
        LEFT JOIN users user2
        ON (page.updated_by = user2.id)
        WHERE page.id = ? AND page.deleted = 0
    '''
    return database_utils.execute_query(sql, page_id, single=True)


def insert(data: dict[str, Any]) -> int:
    """
    Insert page to database and return the ID.
    """
    sql = '''
        INSERT INTO pages (
            idiom,
            name,
            layout,
            created_by,
            updated_by,
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
            properties,
            json)
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    page_id = database_utils.execute_update(
        sql,
        (
            data['idiom'],
            data['name'],
            data['layout'],
            data['created_by'],
            data['updated_by'],
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
            data['properties'],
            data['json'],
        )
    )
    return int(page_id)


def update(page_id: int, data: dict[str, Any]) -> None:
    """
    Update page.
    """
    sql = '''
        UPDATE pages SET
            idiom = ?,
            layout = ?,
            created_by = ?,
            updated_by = ?,
            updated_on = CURRENT_TIMESTAMP,
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
            properties = ?,
            json = ?,
            active = ?
        WHERE
            id = ?
    '''
    database_utils.execute_update(
        sql,
        (
            data['idiom'],
            data['layout'],
            data['created_by'],
            data['updated_by'],
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
            data['properties'],
            data['json'],
            data['active'],
            page_id
        )
    )

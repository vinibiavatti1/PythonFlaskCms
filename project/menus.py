from typing import Union
from project.utils.translation_utils import t


###############################################################################
# Menus Build Functions
###############################################################################


def build_public_menu() -> list[dict]:
    """
    Return a list with menus for public area
    """
    return [
        {
            'header': t('menus.headers.menu'),
        },
        {
            'title': t('menus.homepage'),
            'link': '/',
            'icon': 'bi-house',
        },
        {
            'title': t('menus.search'),
            'modal': '#search-modal',
            'icon': 'bi-search',
        },
        {
            'title': t('menus.login'),
            'link': '/login',
            'icon': 'bi-box-arrow-in-right',
        },
    ]

def build_private_menu() -> list[Union[tuple, str]]:
    """
    Return a list with menus for member area
    """
    return []


def build_admin_manu() -> list[dict]:
    """
    Return a list with menus for admin area
    """
    return [
        {
            'header': 'Website',
        },
        {
            'title': 'Pages',
            'link': '/admin/pages',
            'icon': 'bi-filetype-html',
        },
        {
            'title': 'Menus',
            'link': '/',
            'icon': 'bi-list',
        },
        {
            'header': 'Blog',
        },
        {
            'title': 'Posts',
            'link': '/admin/posts',
            'icon': 'bi-newspaper',
        },
        {
            'title': 'Tags',
            'link': '/admin/posts',
            'icon': 'bi-tags',
        },
        {
            'header': 'Configuration',
        },
        {
            'title': 'Properties',
            'link': '/',
            'icon': 'bi-gear',
        },
        {
            'header': 'Administration',
        },
        {
            'title': 'Adm. Users',
            'link': '/',
            'icon': 'bi-people',
        },
        {
            'title': 'Adm. User Roles',
            'link': '/',
            'icon': 'bi-person-check',
        },
        {
            'header': t('menus.headers.menu'),
        },
        {
            'title': t('menus.homepage'),
            'link': '/',
            'icon': 'bi-house',
        },
        {
            'title': t('menus.map'),
            'link': '/admin/map',
            'icon': 'bi-map',
        },
        {
            'title': t('menus.chart'),
            'link': '/admin/chart',
            'icon': 'bi-bar-chart',
        },
        {
            'title': t('menus.list'),
            'link': '/admin/list',
            'icon': 'bi-table',
        },
        {
            'title': t('menus.form'),
            'link': '/admin/form',
            'icon': 'bi-ui-checks',
        },
        {
            'title': t('menus.calendar'),
            'link': '/admin/calendar',
            'icon': 'bi-calendar-date',
        },
        {
            'title': t('menus.search'),
            'modal': '#search-modal',
            'icon': 'bi-search',
        },
        {
            'header': t('menus.headers.user'),
        },
        {
            'title': t('menus.logout'),
            'link': '/logout',
            'icon': 'bi-box-arrow-in-right',
        },
    ]

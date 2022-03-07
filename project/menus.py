from typing import Union
from project.utils.translation_utils import t
from project.models.header_model import HeaderModel
from project.models.menu_model import MenuModel


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


def build_admin_manu() -> list[Union[MenuModel, HeaderModel]]:
    """
    Return a list with menus for admin area
    """
    return [
        HeaderModel(
            'Website'
        ),
        MenuModel(
            title='Pages',
            link='/admin/pages',
            icon='bi-filetype-html',
        ),
        MenuModel(
            title='Menus',
            link='/admin/pages',
            icon='bi-list',
        ),
        HeaderModel(
            'Blog'
        ),
        MenuModel(
            title='Posts',
            link='/admin/posts',
            icon='bi-newspaper',
        ),
        MenuModel(
            title='Tags',
            link='/admin/posts',
            icon='bi-tags',
        ),
        HeaderModel(
            'Configuration'
        ),
        MenuModel(
            title='Properties',
            link='/admin/posts',
            icon='bi-gear',
        ),
        HeaderModel(
            'Administration'
        ),
        MenuModel(
            title='Adm. Users',
            link='/admin/posts',
            icon='bi-people',
        ),
        MenuModel(
            title='Adm. User Roles',
            link='/admin/posts',
            icon='bi-person-check',
        ),
    ]

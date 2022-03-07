"""
Admin menu registry.
"""
from typing import Union
from project.models.header_model import HeaderModel
from project.models.menu_model import MenuModel


admin_menu: list[Union[MenuModel, HeaderModel]] = [

    ###########################################################################
    # Website
    ###########################################################################

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

    ###########################################################################
    # Blog
    ###########################################################################

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

    ###########################################################################
    # Configuration
    ###########################################################################

    HeaderModel(
        'Configuration'
    ),
    MenuModel(
        title='Properties',
        link='/admin/properties',
        icon='bi-gear',
    ),

    ###########################################################################
    # Administration
    ###########################################################################

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
    # Add more ...
]

"""
Admin menu records module.
"""
from typing import Union
from project.models.header_model import HeaderModel
from project.models.menu_model import MenuModel


menu: list[Union[MenuModel, HeaderModel]] = [

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
        link='/admin/menus',
        icon='bi-list',
    ),
    MenuModel(
        title='Blog Posts',
        link='/admin/posts',
        icon='bi-newspaper',
    ),
    MenuModel(
        title='FAQs',
        link='/admin/posts',
        icon='bi-question-circle',
    ),
    MenuModel(
        title='Medias',
        link='/admin/posts',
        icon='bi-image',
    ),
    MenuModel(
        title='Translations',
        link='/admin/translations',
        icon='bi-translate',
    ),
    MenuModel(
        title='Redirects',
        link='/admin/redirects',
        icon='bi-signpost-split',
    ),

    ###########################################################################
    # Configuration
    ###########################################################################

    HeaderModel(
        'Configuration'
    ),
    MenuModel(
        title='Sitemap',
        link='/admin/sitemap',
        icon='bi-map',
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
        title='Users',
        link='/admin/posts',
        icon='bi-people',
    ),
    # Add more ...
]

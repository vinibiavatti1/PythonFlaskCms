"""
Admin menu records module.
"""
from typing import Union
from project.models.header_model import HeaderModel
from project.models.menu_item_model import MenuItemModel


menu_records: list[Union[MenuItemModel, HeaderModel]] = [

    ###########################################################################
    # Objects
    ###########################################################################

    HeaderModel(
        title='Objects'
    ),
    MenuItemModel(
        title='Contents',
        link='/object/contents',
        icon='bi-files',
    ),
    MenuItemModel(
        title='Resources',
        link='/object/resources',
        icon='bi-box-seam',
    ),
    MenuItemModel(
        title='Pages',
        link='/object/pages',
        icon='bi-file-earmark-code',
    ),
    MenuItemModel(
        title='Trash Bin',
        link='/trash_bin',
        icon='bi-trash',
    ),

    ###########################################################################
    # Assets
    ###########################################################################

    HeaderModel(
        title='Assets'
    ),
    MenuItemModel(
        title='Files',
        link='/files',
        icon='bi-file-earmark-image',
    ),

    ###########################################################################
    # Components
    ###########################################################################

    HeaderModel(
        title='Components'
    ),
    MenuItemModel(
        title='Navbar',
        link='/navbar',
        icon='bi-window',
    ),
    MenuItemModel(
        title='Footer',
        link='/footer',
        icon='bi-window-desktop',
    ),

    ###########################################################################
    # Configuration
    ###########################################################################

    HeaderModel(
        title='Configuration'
    ),
    MenuItemModel(
        title='Properties',
        link='/properties',
        icon='bi-gear',
    ),
    MenuItemModel(
        title='Users',
        link='/pages',
        icon='bi-people',
    ),
    MenuItemModel(
        title='Logout',
        link='/logout',
        icon='bi-box-arrow-left',
    ),
]

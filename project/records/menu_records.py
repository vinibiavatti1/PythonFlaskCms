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
        title='Structure'
    ),
    MenuItemModel(
        title='Objects',
        link='/objects',
        icon='bi-boxes',
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
    # Forms
    ###########################################################################

    HeaderModel(
        title='Forms'
    ),
    MenuItemModel(
        title='Entries',
        link='/entries',
        icon='bi-inbox-fill',
        badge_id='entries_badge'
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
        title='Import/Export',
        link='/import_export',
        icon='bi-arrow-left-right',
    ),
    MenuItemModel(
        title='Logout',
        link='/logout',
        icon='bi-box-arrow-left',
    ),
]

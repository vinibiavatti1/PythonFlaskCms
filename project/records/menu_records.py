"""
Admin menu records module.
"""
from typing import Union
from project.models.header_model import HeaderModel
from project.models.menu_item_model import MenuItemModel


menu_records: list[Union[MenuItemModel, HeaderModel]] = [

    ###########################################################################
    # Content
    ###########################################################################

    HeaderModel(
        title='Content'
    ),
    MenuItemModel(
        title='Articles',
        link='/articles',
        icon='bi-files',
    ),
    MenuItemModel(
        title='Landing Pages',
        link='/landing_pages',
        icon='bi-layers',
    ),
    MenuItemModel(
        title='Events',
        link='/events',
        icon='bi-calendar-event',
    ),
    MenuItemModel(
        title='News',
        link='/news',
        icon='bi-newspaper',
    ),
    MenuItemModel(
        title='Posts',
        link='/posts',
        icon='bi-pin-angle',
    ),
    MenuItemModel(
        title='FAQs',
        link='/faqs',
        icon='bi-question-circle',
    ),
    MenuItemModel(
        title='Custom Pages',
        link='/custom_pages',
        icon='bi-filetype-html',
    ),
    MenuItemModel(
        title='Trash Bin',
        link='/trash_bin',
        icon='bi-trash',
    ),

    ###########################################################################
    # Pages
    ###########################################################################

    HeaderModel(
        title='Pages'
    ),
    MenuItemModel(
        title='Article List',
        link='/pages',
        icon='bi-file-earmark-post',
    ),
    MenuItemModel(
        title='Event List',
        link='/pages',
        icon='bi-file-earmark-medical',
    ),
    MenuItemModel(
        title='News List',
        link='/news_list',
        icon='bi-file-earmark-easel',
    ),
    MenuItemModel(
        title='FAQ List',
        link='/pages',
        icon='bi-file-earmark-text',
    ),
    MenuItemModel(
        title='Calendar',
        link='/pages',
        icon='bi-calendar',
    ),
    MenuItemModel(
        title='Search',
        link='/pages',
        icon='bi-search',
    ),
    MenuItemModel(
        title='Login',
        link='/pages',
        icon='bi-key',
    ),
    MenuItemModel(
        title='Contact',
        link='/pages',
        icon='bi-file-earmark-person',
    ),
    MenuItemModel(
        title='Sitemap',
        link='/pages',
        icon='bi-map',
    ),
    MenuItemModel(
        title='Blog',
        link='/pages',
        icon='bi-postage',
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
        title='Translations',
        link='/translations',
        icon='bi-translate',
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

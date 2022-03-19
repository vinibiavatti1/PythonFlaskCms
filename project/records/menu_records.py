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
        link='/admin/articles',
        icon='bi-files',
    ),
    MenuItemModel(
        title='Landing Pages',
        link='/admin/landing-pages',
        icon='bi-layers',
    ),
    MenuItemModel(
        title='Events',
        link='/admin/events',
        icon='bi-calendar-event',
    ),
    MenuItemModel(
        title='Posts',
        link='/admin/posts',
        icon='bi-pin-angle',
    ),
    MenuItemModel(
        title='FAQs',
        link='/admin/faqs',
        icon='bi-question-circle',
    ),
    MenuItemModel(
        title='Custom Pages',
        link='/admin/custom-pages',
        icon='bi-filetype-html',
    ),
    MenuItemModel(
        title='Trash Bin',
        link='/admin/trash-bin',
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
        link='/admin/pages',
        icon='bi-file-earmark-post',
    ),
    MenuItemModel(
        title='Event List',
        link='/admin/pages',
        icon='bi-file-earmark-medical',
    ),
    MenuItemModel(
        title='FAQ List',
        link='/admin/pages',
        icon='bi-file-earmark-text',
    ),
    MenuItemModel(
        title='Calendar',
        link='/admin/pages',
        icon='bi-calendar',
    ),
    MenuItemModel(
        title='Search',
        link='/admin/pages',
        icon='bi-search',
    ),
    MenuItemModel(
        title='Login',
        link='/admin/pages',
        icon='bi-key',
    ),
    MenuItemModel(
        title='Contact',
        link='/admin/pages',
        icon='bi-file-earmark-person',
    ),
    MenuItemModel(
        title='Sitemap',
        link='/admin/pages',
        icon='bi-map',
    ),
    MenuItemModel(
        title='Blog',
        link='/admin/pages',
        icon='bi-postage',
    ),

    ###########################################################################
    # Media
    ###########################################################################

    HeaderModel(
        title='Media'
    ),
    MenuItemModel(
        title='Images',
        link='/admin/pages',
        icon='bi-file-earmark-image',
    ),
    MenuItemModel(
        title='Videos',
        link='/admin/pages',
        icon='bi-file-earmark-play',
    ),
    MenuItemModel(
        title='Files',
        link='/admin/pages',
        icon='bi-file-earmark',
    ),

    ###########################################################################
    # Components
    ###########################################################################

    HeaderModel(
        title='Components'
    ),
    MenuItemModel(
        title='Navbar',
        link='/admin/pages',
        icon='bi-window',
    ),
    MenuItemModel(
        title='Footer',
        link='/admin/pages',
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
        link='/admin/pages',
        icon='bi-gear',
    ),
    MenuItemModel(
        title='Translations',
        link='/admin/pages',
        icon='bi-translate',
    ),
    MenuItemModel(
        title='Users',
        link='/admin/pages',
        icon='bi-people',
    ),
    MenuItemModel(
        title='Logout',
        link='/admin/pages',
        icon='bi-box-arrow-left',
    ),
]

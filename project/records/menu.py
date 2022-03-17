"""
Admin menu records module.
"""
from typing import Union
from project.models.header_model import HeaderModel
from project.models.menu_model import MenuModel


menu: list[Union[MenuModel, HeaderModel]] = [

    ###########################################################################
    # Content
    ###########################################################################

    HeaderModel(
        title='Content'
    ),
    MenuModel(
        title='Articles',
        link='/admin/articles',
        icon='bi-files',
    ),
    MenuModel(
        title='Landing Pages',
        link='/admin/landing-pages',
        icon='bi-layers',
    ),
    MenuModel(
        title='Events',
        link='/admin/events',
        icon='bi-calendar-event',
    ),
    MenuModel(
        title='Posts',
        link='/admin/posts',
        icon='bi-pin-angle',
    ),
    MenuModel(
        title='FAQs',
        link='/admin/faqs',
        icon='bi-question-circle',
    ),
    MenuModel(
        title='Custom Pages',
        link='/admin/custom-pages',
        icon='bi-filetype-html',
    ),

    ###########################################################################
    # Pages
    ###########################################################################

    HeaderModel(
        title='Pages'
    ),
    MenuModel(
        title='Article List',
        link='/admin/pages',
        icon='bi-file-earmark-post',
    ),
    MenuModel(
        title='Event List',
        link='/admin/pages',
        icon='bi-file-earmark-medical',
    ),
    MenuModel(
        title='FAQ List',
        link='/admin/pages',
        icon='bi-file-earmark-text',
    ),
    MenuModel(
        title='Calendar',
        link='/admin/pages',
        icon='bi-calendar',
    ),
    MenuModel(
        title='Search',
        link='/admin/pages',
        icon='bi-search',
    ),
    MenuModel(
        title='Login',
        link='/admin/pages',
        icon='bi-key',
    ),
    MenuModel(
        title='Contact',
        link='/admin/pages',
        icon='bi-file-earmark-person',
    ),
    MenuModel(
        title='Sitemap',
        link='/admin/pages',
        icon='bi-map',
    ),
    MenuModel(
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
    MenuModel(
        title='Images',
        link='/admin/pages',
        icon='bi-file-earmark-image',
    ),
    MenuModel(
        title='Videos',
        link='/admin/pages',
        icon='bi-file-earmark-play',
    ),
    MenuModel(
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
    MenuModel(
        title='Navbar',
        link='/admin/pages',
        icon='bi-window',
    ),
    MenuModel(
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
    MenuModel(
        title='Properties',
        link='/admin/pages',
        icon='bi-gear',
    ),
    MenuModel(
        title='Translations',
        link='/admin/pages',
        icon='bi-translate',
    ),
    MenuModel(
        title='Users',
        link='/admin/pages',
        icon='bi-people',
    ),
    MenuModel(
        title='Logout',
        link='/admin/pages',
        icon='bi-box-arrow-left',
    ),
]

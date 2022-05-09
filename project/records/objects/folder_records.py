"""
Folder records.
"""
from project.models.object_model import ObjectModel
from project.enums import object_enum


folder_records: list[ObjectModel] = [
    ObjectModel(
        name=object_enum.PAGES_FOLDER,
        description='Pages folder',
        icon='bi-folder',
        is_root=True,
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.ARTICLE_PAGE,
            object_enum.EVENT_PAGE,
            object_enum.NEWS_PAGE,
            object_enum.FAQ_PAGE,
            object_enum.CALENDAR_PAGE,
            object_enum.SEARCH_PAGE,
            object_enum.LOGIN_PAGE,
            object_enum.CONTACT_PAGE,
            object_enum.BLOG_PAGE,
        ],
    ),
    ObjectModel(
        name=object_enum.COMPONENTS_FOLDER,
        description='Components folder',
        icon='bi-folder',
        is_root=True,
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.NAVBAR_COMPONENT,
            object_enum.FOOTER_COMPONENT,
        ],
    ),
    ObjectModel(
        name=object_enum.RESOURCES_FOLDER,
        description='Resources folder',
        icon='bi-folder',
        is_root=True,
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.TRANSLATIONS_FOLDER,
            object_enum.ANNOUNCEMENTS_FOLDER,
            object_enum.REDIRECTS_FOLDER,
        ],
    ),
    ObjectModel(
        name=object_enum.TRANSLATIONS_FOLDER,
        description='Translations folder',
        icon='bi-folder',
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.TRANSLATION_RESOURCE,
        ],
    ),
    ObjectModel(
        name=object_enum.ANNOUNCEMENTS_FOLDER,
        description='Annoucements folder',
        icon='bi-folder',
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.ANNOUNCEMENT_RESOURCE,
        ],
    ),
    ObjectModel(
        name=object_enum.REDIRECTS_FOLDER,
        description='Redirects folder',
        icon='bi-folder',
        is_content=False,
        properties=[],
        allow_actions=False,
        template=None,
        children=[
            object_enum.REDIRECT_RESOURCE,
        ],
    ),
]

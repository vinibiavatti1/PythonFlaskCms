"""
Resource records.
"""
from project.models.object_model import ObjectModel
from project.enums import object_enum
from project.properties.resources.announcement_properties \
    import announcement_properties
from project.properties.resources.translation_properties \
    import translation_properties
from project.properties.resources.redirect_properties \
    import redirect_properties
from project.properties.resources.faq_properties import \
    faq_properties


resource_records: list[ObjectModel] = [
    ObjectModel(
        name=object_enum.TRANSLATION_RESOURCE,
        description='Translation resource',
        icon='bi-translate',
        is_content=False,
        properties=translation_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),
    ObjectModel(
        name=object_enum.FAQ_RESOURCE,
        description='FAQ resource',
        icon='bi-question-circle',
        is_content=False,
        properties=faq_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),
    ObjectModel(
        name=object_enum.REDIRECT_RESOURCE,
        description='Redirect resource',
        icon='bi-signpost-split',
        is_content=False,
        properties=redirect_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),
    ObjectModel(
        name=object_enum.ANNOUNCEMENT_RESOURCE,
        description='Annoucement resource',
        icon='bi-megaphone',
        is_content=False,
        properties=announcement_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),
]

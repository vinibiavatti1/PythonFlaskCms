"""
Resource records module.
"""
from project.models.resource_type_model import ResourceTypeModel
from project.enums import object_subtype_enum
from project.properties.resources.translation_properties import \
    translation_properties
from project.properties.resources.faq_properties import \
    faq_properties
from project.properties.resources.redirect_properties import \
    redirect_properties
from project.properties.resources.announcement_properties import \
    announcement_properties


resource_type_records: list[ResourceTypeModel] = [
    ResourceTypeModel(
        label='Translation',
        name=object_subtype_enum.TRANSLATION_RESOURCE,
        icon='bi-translate',
        properties=translation_properties,
    ),
    ResourceTypeModel(
        label='FAQ',
        name=object_subtype_enum.FAQ_RESOURCE,
        icon='bi-question-circle',
        properties=faq_properties,
    ),
    ResourceTypeModel(
        label='Redirect',
        name=object_subtype_enum.REDIRECT_RESOURCE,
        icon='bi-signpost-split',
        properties=redirect_properties,
    ),
    ResourceTypeModel(
        label='Announcement',
        name=object_subtype_enum.ANNOUNCEMENT_RESOURCE,
        icon='bi-megaphone',
        properties=announcement_properties,
    ),
    # Add more...
]

"""
Resource records module.
"""
from project.models.record_type_model import RecordTypeModel
from project.enums import object_subtype_enum
from project.properties.resources.translation_properties import \
    translation_properties
from project.properties.resources.faq_properties import \
    faq_properties
from project.properties.resources.redirect_properties import \
    redirect_properties
from project.properties.resources.announcement_properties import \
    announcement_properties


resource_type_records: list[RecordTypeModel] = [
    RecordTypeModel(
        label='Translation',
        name=object_subtype_enum.TRANSLATION_RESOURCE,
        icon='bi-translate',
        properties=translation_properties,
    ),
    RecordTypeModel(
        label='FAQ',
        name=object_subtype_enum.FAQ_RESOURCE,
        icon='bi-question-circle',
        properties=faq_properties,
    ),
    RecordTypeModel(
        label='Redirect',
        name=object_subtype_enum.REDIRECT_RESOURCE,
        icon='bi-signpost-split',
        properties=redirect_properties,
    ),
    RecordTypeModel(
        label='Announcement',
        name=object_subtype_enum.ANNOUNCEMENT_RESOURCE,
        icon='bi-megaphone',
        properties=announcement_properties,
    ),
    # Add more...
]

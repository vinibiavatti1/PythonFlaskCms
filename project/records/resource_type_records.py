"""
Resource records module.
"""
from project.models.resource_type_model import ResourceTypeModel
from project.properties.resources.translation_properties import \
    translation_properties
from project.properties.resources.faq_properties import \
    faq_properties
from project.properties.resources.redirect_properties import \
    redirect_properties


resource_type_records: list[ResourceTypeModel] = [
    ResourceTypeModel(
        label='Translation',
        name='translation',
        icon='bi-translate',
        properties=translation_properties,
    ),
    ResourceTypeModel(
        label='FAQ',
        name='faq',
        icon='bi-question-circle',
        properties=faq_properties,
    ),
    ResourceTypeModel(
        label='Redirect',
        name='redirect',
        icon='bi-signpost-split',
        properties=redirect_properties,
    ),
    # Add more...
]

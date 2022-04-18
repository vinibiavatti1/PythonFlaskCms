"""
Component type records module.
"""
from project.models.record_type_model import RecordTypeModel
from project.enums import object_subtype_enum
from project.models.property_model import PropertyModel
from project.enums import string_types_enum as str_type
from project.enums import nested_object_type_enum
from project.properties.components.navbar_properties import navbar_properties
from project.properties.components.footer_properties import footer_properties


component_type_records: list[RecordTypeModel] = [
    RecordTypeModel(
        label='Navbar',
        name=object_subtype_enum.NAVBAR_COMPONENT,
        icon='bi-window',
        properties=navbar_properties,
        allow_deleted=False,
        allow_duplicated=False,
        nested_objects=[
            nested_object_type_enum.NAVBAR_LINKS,
        ]
    ),
    RecordTypeModel(
        label='Footer',
        name=object_subtype_enum.FOOTER_COMPONENT,
        icon='bi-window-desktop',
        properties=footer_properties,
        allow_deleted=False,
        allow_duplicated=False,
        nested_objects=[
            nested_object_type_enum.FOOTER_LINKS,
        ]
    ),
    # Add more...
]

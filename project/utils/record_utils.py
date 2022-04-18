"""
Record utilities.
"""
from typing import Optional
from project.models.record_type_model import RecordTypeModel
from project.enums import object_type_enum
from project.records.content_type_records import content_type_records
from project.records.page_type_records import page_type_records
from project.records.resource_type_records import resource_type_records
from project.records.component_type_records import component_type_records


def get_record_by_name(name: str, record_list: list[RecordTypeModel]
                       ) -> Optional[RecordTypeModel]:
    """
    Generic function to get record by name.
    """
    for record in record_list:
        if hasattr(record, 'name') and getattr(record, 'name') == name:
            return record
    return None


def get_record_list_by_object_type(object_type: str
                                   ) -> Optional[list[RecordTypeModel]]:
    """
    Return object type record list by object type name.
    """
    if object_type == object_type_enum.CONTENT:
        return content_type_records
    elif object_type == object_type_enum.RESOURCE:
        return resource_type_records
    elif object_type == object_type_enum.COMPONENT:
        return component_type_records
    elif object_type == object_type_enum.PAGE:
        return page_type_records
    return None

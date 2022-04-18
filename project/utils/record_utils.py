"""
Record utilities.
"""
from typing import Optional
from project.models.object_model import ObjectModel
from project.models.record_type_model import RecordTypeModel
from project.enums import object_enum
from project.records.object_records import object_records


def get_record_by_name(name: str) -> Optional[ObjectModel]:
    """
    Get object record by name.
    """
    for record in object_records:
        if record.name == name:
            return record
    return None


def get_records_by_names(names: list[str]) -> list[ObjectModel]:
    """
    Get objects by list of names.
    """
    records = []
    for name in names:
        record = get_record_by_name(name)
        if record:
            records.append(record)
    return records


def get_root_records() -> list[ObjectModel]:
    """
    Get root records.
    """
    result = []
    for record in object_records:
        if record.is_root:
            result.append(record)
    return result


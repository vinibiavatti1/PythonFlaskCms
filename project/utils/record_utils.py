"""
Record utilities.
"""
from typing import Optional
from project.models.content_type_model import ContentTypeModel
from project.records.content_type_records import content_type_records


def get_content_record(name: str) -> Optional[ContentTypeModel]:
    """
    Get content type record by name.
    """
    for record in content_type_records:
        if record.name == name:
            return record
    return None

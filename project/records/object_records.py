"""
Object records.
"""
from project.models.object_model import ObjectModel
from project.records.objects.folder_records import folder_records
from project.records.objects.content_records import content_records
from project.records.objects.page_records import page_records
from project.records.objects.component_records import component_records
from project.records.objects.resource_records import resource_records


object_records: list[ObjectModel] = []
object_records.extend(folder_records)
object_records.extend(page_records)
object_records.extend(content_records)
object_records.extend(component_records)
object_records.extend(resource_records)

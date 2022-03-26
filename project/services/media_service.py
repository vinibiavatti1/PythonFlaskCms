"""
Media service.
"""
from flask import current_app
from project.models.media_model import MediaModel
from project.utils import file_utils
from project.services import property_service
import os


def select_all(context: str, page: int) -> list[MediaModel]:
    """
    Select all media files.
    """
    media_page_size = property_service.get_property(context, 'media_page_size')
    if not media_page_size:
        media_page_size = '60'
    media_path = os.path.join(str(current_app.static_folder), 'medias')
    medias = list()
    names = os.listdir(media_path)
    for name in names:
        if os.path.isdir(name):
            continue
        medias.append(MediaModel(
            path=os.path.join('/static/medias', name),
            name=file_utils.get_file_name(name),
            extension=file_utils.get_file_extension(name),
            file_type=file_utils.get_file_type(name),
        ))
    if page == 0:
        return medias
    page -= 1
    if page < 0:
        page = 0
    page_size = int(media_page_size)
    range_start = page_size * page
    range_stop = page_size * (page + 1)
    slice_ = slice(range_start, range_stop)
    return medias[slice_]

"""
File service.
"""
from typing import Any, Callable
from flask import current_app
from project.models.file_model import FileModel
from project.utils import file_utils
from project.services import property_service
import os


FILES_FOLDER = 'files'
DELETED_MARK = 'DELETED_'


join: Callable[..., Any] = os.path.join


def select_all(context: str, page: int) -> list[FileModel]:
    """
    Select all media files.
    """
    media_page_size = property_service.get_property_value(
        context, 'media_page_size'
    )
    if not media_page_size:
        media_page_size = '60'
    files = get_all_files()
    if page == 0:
        return files
    page -= 1
    if page < 0:
        page = 0
    page_size = int(media_page_size)
    range_start = page_size * page
    range_stop = page_size * (page + 1)
    slice_ = slice(range_start, range_stop)
    return files[slice_]


def select_all_by_type(file_type: str) -> list[FileModel]:
    """
    Select all files by file type.
    """
    return [file for file in get_all_files() if file.file_type == file_type]


def get_all_files() -> list[FileModel]:
    """
    Get all files from static folder.
    """
    files_path = join(str(current_app.static_folder), FILES_FOLDER)
    files = list()
    names = os.listdir(files_path)
    for name in names:
        if os.path.isdir(name) or name.startswith(DELETED_MARK):
            continue
        files.append(FileModel(
            path=join('/static', FILES_FOLDER, name),
            name=file_utils.get_file_name(name),
            extension=file_utils.get_file_extension(name),
            file_type=file_utils.get_file_type(name),
        ))
    return files


def upload_files(files: list[Any], replace: bool) -> None:
    """
    Upload media files to static folder.
    """
    files_path = join(str(current_app.static_folder), FILES_FOLDER)
    for file in files:
        file_name = file.filename
        index = 0
        initial_file_path = join(files_path, file_name)
        file_path = initial_file_path
        while not replace and os.path.exists(file_path):
            file_path = file_utils.append_index_to_file_name(
                initial_file_path,
                index
            )
            index += 1
        file.save(join(
            current_app.config['UPLOAD_FOLDER'],
            file_utils.get_file_name(file_path),
        ))


def delete_file(file_name: str) -> None:
    """
    Delete file from static folder.
    """
    files_path = join(str(current_app.static_folder), FILES_FOLDER)
    file_path = join(files_path, file_name)
    if os.path.exists(file_path):
        os.rename(
            file_path,
            join(files_path, DELETED_MARK + file_name)
        )

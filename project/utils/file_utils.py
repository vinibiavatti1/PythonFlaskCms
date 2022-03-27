"""
File utilities.
"""
import os
from project.enums import file_extensions_enum
from project.enums import file_type_enum
from flask import current_app


def get_file_extension(path: str) -> str:
    """
    Get file extension from path.
    """
    split = os.path.splitext(path)
    if not len(split):
        return ''
    extension = split[-1].lower()
    return extension.replace('.', '')


def get_file_name(path: str) -> str:
    """
    Get the file name with extension.
    """
    return os.path.basename(path)


def get_file_dir(path: str) -> str:
    """
    Get the dirname of the file.
    """
    return os.path.dirname(path)


def get_file_name_without_extension(path: str) -> str:
    """
    Get the file name without extension.
    """
    return os.path.splitext(path)[0]


def get_file_type(path: str) -> str:
    """
    Get file type by file extension.
    """
    extension = get_file_extension(path)
    if extension in file_extensions_enum.IMAGE_FILE:
        return file_type_enum.IMAGE
    elif extension in file_extensions_enum.VIDEO_FILE:
        return file_type_enum.VIDEO
    return file_type_enum.FILE


def append_index_to_file_name(path: str, index: int) -> str:
    """
    Append index to file name.
    """
    dir_name = get_file_dir(path)
    file_name = get_file_name(path)
    extension = get_file_extension(file_name)
    file_name_without_ext = get_file_name_without_extension(file_name)
    file_name_without_ext += '_' + str(index)
    current_app.logger.info(os.path.join(
        dir_name,
        file_name_without_ext + '.' + extension
    ))
    return os.path.join(
        dir_name,
        file_name_without_ext + '.' + extension
    )

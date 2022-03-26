"""
File utilities.
"""
import os
from project.enums import file_extensions_enum
from project.enums import file_type_enum


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

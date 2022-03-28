"""
Media service module.
"""
from io import BytesIO
from typing import Optional
from flask import current_app
from PIL import Image
import os
from project.enums import file_extensions_enum
from project.utils import file_utils


FILES_FOLDER = 'files'


def get_image(image_name: str, *,
              crop_x: Optional[int] = None,
              crop_y: Optional[int] = None,
              crop_width: Optional[int] = None,
              crop_height: Optional[int] = None,
              resize_width: Optional[int] = None,
              resize_height: Optional[int] = None) -> Image:
    """
    Get and crop image from static directory.
    """
    # Get image path
    image_path = os.path.join(
        str(current_app.static_folder),
        FILES_FOLDER,
        image_name,
    )

    # Validate exists
    if not os.path.exists(image_path):
        raise ValueError(f'The file {image_name} was not found')

    # Validate directory
    if os.path.isdir(image_path):
        raise ValueError(f'Invalid image')

    # Validate extension
    extension = file_utils.get_file_extension(image_path)
    if extension not in file_extensions_enum.IMAGE_FILE:
        raise ValueError(f'Invalid image format: {extension}')

    # Crop image
    image = Image.open(image_path)
    if (crop_x is not None and crop_y is not None and
            crop_width is not None and crop_height is not None):
        image = image.crop((crop_x, crop_y, crop_width, crop_height))
    if resize_width and resize_height:
        image = image.resize((resize_width, resize_height))
    return image


def store_image_in_memory(image: Image) -> BytesIO:
    """
    Store image into memory and return it.
    """
    img_io = BytesIO()
    image.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return img_io

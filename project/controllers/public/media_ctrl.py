"""
Media controller.
"""
from typing import Any
from flask import Blueprint, abort, current_app, request, flash, send_file
from project.services import media_service


# Controller data
CONTROLLER_NAME = 'admin_media_ctrl'
URL_PREFIX = '/media'
PAGE_TITLE = 'Files'


# Blueprint data
blueprint = Blueprint(
    CONTROLLER_NAME,
    __name__,
    url_prefix=URL_PREFIX
)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/<image_name>', methods=['GET'])
def list_view(image_name: str) -> Any:
    """
    Render image with crop parameters.
    """
    try:
        crop_x = request.args.get('x', type=int)
        crop_y = request.args.get('y', type=int)
        crop_width = request.args.get('width', type=int)
        crop_height = request.args.get('height', type=int)
        resize_width = request.args.get('rwidth', type=int)
        resize_height = request.args.get('rheight', type=int)
        image = media_service.get_image(
            image_name=image_name,
            crop_x=crop_x,
            crop_y=crop_y,
            crop_width=crop_width,
            crop_height=crop_height,
            resize_width=resize_width,
            resize_height=resize_height,
        )
        image_file = media_service.store_image_in_memory(image)
        return send_file(image_file, mimetype='image/jpeg')
    except Exception as err:
        raise err

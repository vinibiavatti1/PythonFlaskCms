"""
Media controller.
"""
from typing import Any
from flask import Blueprint, redirect, render_template, request
from project.enums import resource_type_enum
from project.decorators.security_decorators import login_required
from project.properties.article_properties import article_properties
from project.decorators.context_decorators import process_context
from project.services import media_service


# Controller data
CONTROLLER_NAME = 'admin_media_ctrl'
URL_PREFIX = '/<context>/admin/media'
PAGE_TITLE = 'Media Files'


# Blueprint data
blueprint = Blueprint(
    CONTROLLER_NAME,
    __name__,
    url_prefix=URL_PREFIX
)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/', methods=['GET'], defaults={'page': 1})
@blueprint.route('/<int:page>', methods=['GET'])
@login_required()
@process_context()
def list_view(context: str, page: int = 1) -> Any:
    """
    Render list page.
    """
    medias = media_service.select_all(context, page)
    first_page_url = f'/{context}/admin/media'
    prev_page_url = f'/{context}/admin/media/{page - 1 if page != 0 else 1}'
    next_page_url = f'/{context}/admin/media/{page + 1}'
    all_page_url = f'/{context}/admin/media/0'
    return render_template(
        '/admin/media_list.html',
        page_data=dict(
            title=PAGE_TITLE,
            action_url=f'/{context}/admin/media/upload',
            medias=medias,
            first_page_url=first_page_url,
            prev_page_url=prev_page_url,
            next_page_url=next_page_url,
            all_page_url=all_page_url,
            page=page,
        )
    )


@blueprint.route('/upload', methods=['POST'])
@login_required()
@process_context()
def upload_action(context: str) -> Any:
    """
    Upload media endpoint.
    """

    return redirect(request.referrer)

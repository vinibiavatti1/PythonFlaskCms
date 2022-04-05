"""
Redirects controller.
"""
from typing import Any
from flask import Blueprint, request, render_template
from project.enums import object_subtype_enum
from project.decorators.security_decorators import login_required
from project.properties.redirect_properties import redirect_properties
from project.decorators.context_decorators import process_context
from project.utils.ctrl_utils import get_object_root_url
from project.processors import content_ctrl_processor
from project.services import object_service


# Controller data
CONTROLLER_NAME = 'admin_redirects_ctrl'
URL_PREFIX = '/<context>/admin/redirects'
PAGE_TITLE = 'Redirects'
LIST_NAME = 'redirects'
RESOURCE_TYPE = object_subtype_enum.REDIRECT
PROPERTIES = redirect_properties


# Blueprint data
blueprint = Blueprint(
    CONTROLLER_NAME,
    __name__,
    url_prefix=URL_PREFIX
)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/', methods=['GET'])
@login_required()
@process_context()
def list_view(context: str) -> Any:
    """
    Render datatable with data.
    """
    list_url = get_object_root_url(context, LIST_NAME)
    headers = [
        '#',
        'Name',
        'Target',
        'Destination',
        'Active',
        'Actions',
    ]
    data: list[Any] = list()
    contents = object_service.select_all_by_type(context, RESOURCE_TYPE)
    for content in contents:
        id_ = content.id
        active = content.properties['active'] == '1'
        data.append((
            id_,
            content.name,
            '<i class="bi bi-broadcast"></i> True' if active else 'False',
            content.created_on,
            f'<a href="{list_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/content_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            title=PAGE_TITLE,
            btn_link=f'{list_url}/create',
        )
    )


@blueprint.route('/create', methods=['GET'])
@login_required()
@process_context()
def create_view(context: str) -> Any:
    """
    Render create page.
    """
    return content_ctrl_processor.process_create_view(
        context,
        RESOURCE_TYPE,
        LIST_NAME,
        PAGE_TITLE,
        PROPERTIES,
    )


@blueprint.route('/edit/<content_id>', methods=['GET'])
@login_required()
@process_context()
def edit_view(context: str, content_id: int) -> Any:
    """
    Render edit page.
    """
    return content_ctrl_processor.process_edit_view(
        context,
        RESOURCE_TYPE,
        LIST_NAME,
        PAGE_TITLE,
        PROPERTIES,
        content_id,
    )


@blueprint.route('/create', methods=['POST'])
@login_required()
@process_context()
def create_action(context: str) -> Any:
    """
    Insert content to database.
    """
    return content_ctrl_processor.process_create_action(
        context,
        RESOURCE_TYPE,
        request.form.to_dict(),
        LIST_NAME,
    )


@blueprint.route('/edit/<content_id>', methods=['POST'])
@login_required()
@process_context()
def edit_action(context: str, content_id: int) -> Any:
    """
    Update content in database.
    """
    return content_ctrl_processor.process_edit_action(
        context,
        RESOURCE_TYPE,
        request.form.to_dict(),
        LIST_NAME,
        content_id,
    )


@blueprint.route('/delete/<content_id>', methods=['GET'])
@login_required()
@process_context()
def delete_action(context: str, content_id: int) -> Any:
    """
    Delete content from database.
    """
    return content_ctrl_processor.process_delete_action(
        context,
        LIST_NAME,
        content_id,
    )


@blueprint.route('/duplicate/<content_id>/<to_context>/<new_name>',
                 methods=['GET'])
@login_required()
@process_context()
def duplicate_action(context: str, content_id: int, to_context: str,
                     new_name: str) -> Any:
    """
    Duplicate content.
    """
    return content_ctrl_processor.process_duplicate_action(
        context,
        LIST_NAME,
        content_id,
        to_context,
        new_name,
    )

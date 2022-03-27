"""
Trash bin controller.
"""
from typing import Any
from werkzeug.utils import redirect
from flask import Blueprint, request, render_template, flash
from project.services import content_service
from project.decorators.security_decorators import login_required
from project.utils.ctrl_utils import get_admin_list_url
from project.decorators.context_decorators import process_context


# Controller properties
CONTROLLER_NAME = 'admin_trash_bin_ctrl'
ROOT_URL = '/<context>/admin/trash_bin'
PAGE_TITLE = 'Trash Bin'
LIST_NAME = 'trash_bin'


# Blueprint
blueprint = Blueprint(
    CONTROLLER_NAME,
    __name__,
    url_prefix=ROOT_URL
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/', methods=['GET'])
@login_required()
@process_context()
def list_view(context: str) -> str:
    """
    Render datatable with data.
    """
    list_url = get_admin_list_url(context, LIST_NAME)
    headers = [
        '#',
        'Name',
        'Content Type',
        'Deleted On',
        'Actions',
    ]
    data: list[Any] = list()
    contents = content_service.select_all_deleted(context)
    for content in contents:
        id_ = content['id']
        data.append((
            id_,
            content['name'],
            str(content['type']).title(),
            content['deleted_on'],
            f'<a href="{list_url}/restore/{id_}">Restore</a>'
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


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/restore/<content_id>', methods=['GET'])
@login_required()
@process_context()
def restore_action(context: str, content_id: int) -> Any:
    """
    Restore content.
    """
    list_url = get_admin_list_url(context, LIST_NAME)
    try:
        content_service.restore(context, content_id)
        flash('Content restored successfully!', category='success')
        return redirect(f'{list_url}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)

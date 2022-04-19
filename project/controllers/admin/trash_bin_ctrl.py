"""
Trash bin controller.
"""
from typing import Any, Optional
from werkzeug.utils import redirect
from flask import Blueprint, request, render_template, flash, abort
from project.decorators.security_decorators import login_required
from project.decorators.context_decorators import process_context
from project.services import object_service
from project.utils.ctrl_utils import generate_admin_url
from project.enums import object_enum
from project.records.object_records import object_records


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


@blueprint.route(
    rule='/',
    methods=['GET'],
    defaults={'object_type': None}
)
@blueprint.route(
    rule='/<object_type>',
    methods=['GET']
)
@login_required()
@process_context()
def list_view(context: str, object_type: Optional[str] = None) -> str:
    """
    Render datatable with data.
    """
    root_url = generate_admin_url(context, 'trash_bin')
    headers = [
        '#',
        'Name',
        'Object Type',
        'Deleted On',
        'Actions',
    ]
    data: list[Any] = list()
    if object_type:
        entities = object_service.select_deleted_by_type(context, object_type)
    else:
        entities = object_service.select_all_deleted(context)
    for entity in entities:
        id_ = entity.id
        object_type = entity.object_type
        record = object_service.get_record_by_name(object_type)
        if record is None:
            return abort(400)

        data.append((
            id_,
            f'<i class="bi {record.icon}"></i> {entity.name}',
            record.name,
            entity.deleted_on,
            f'<a href="{root_url}/restore/{id_}">Restore</a>',
        ))
    return render_template(
        '/admin/trash_bin_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            hide_new_action=True,
            title='Trash Bin',
            root_url=root_url,
            object_type=object_type,
            object_records=object_records,
        )
    )


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/restore/<object_id>', methods=['GET'])
@login_required()
@process_context()
def restore_action(context: str, object_id: int) -> Any:
    """
    Restore content.
    """
    try:
        object_service.restore(object_id)
        flash('Content restored successfully!', category='success')
        return redirect(request.referrer)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)

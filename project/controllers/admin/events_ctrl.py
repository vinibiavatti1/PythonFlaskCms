"""
Events controller.
"""
from typing import Any
from werkzeug.utils import redirect
from flask import Blueprint, request, render_template, flash, abort
from project.models.property_model import PropertyModel
from project.services import content_service
from project.enums import resource_type_enum
from project.decorators.security_decorators import login_required
from project.properties.event_properties import event_properties
from project.utils.data_utils import set_properties_value


# Controller properties
CONTROLLER_NAME = 'admin_events_ctrl'
ROOT_URL = '/admin/events'
RESOURCE_TYPE = resource_type_enum.EVENT
PAGE_TITLE = 'Events'
PROPERTIES = event_properties


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
def list_view() -> str:
    """
    Render datatable with data.
    """
    headers = [
        '#',
        'Name',
        'Private',
        'Published',
        'Created On',
        'Actions',
    ]
    data: list[Any] = list()
    contents = content_service.select_all(RESOURCE_TYPE)
    for content in contents:
        id_ = content['id']
        data.append((
            id_,
            content['name'],
            'True' if content['private'] == 1 else 'False',
            'True' if content['published'] == 1 else 'False',
            content['created_on'],
            f'<a href="{ROOT_URL}/edit/{id_}">Details...</a>'
        ))
    return render_template(
        '/admin/datatable.html',
        page_data=dict(
            headers=headers,
            data=data,
            title=PAGE_TITLE,
            btn_link=f'{ROOT_URL}/create',
        )
    )


@blueprint.route('/create', methods=['GET'])
@login_required()
def create_view() -> str:
    """
    Render create page.
    """
    return render_template(
        '/admin/content.html',
        page_data=dict(
            title=PAGE_TITLE,
            back_url=ROOT_URL,
            action_url=f'{ROOT_URL}/create',
            properties=PROPERTIES,
            content_type=RESOURCE_TYPE,
        )
    )


@blueprint.route('/edit/<content_id>', methods=['GET'])
@login_required()
def edit_view(content_id: int) -> str:
    """
    Render edit page.
    """
    content = content_service.select_by_id(content_id)
    if not content:
        abort(404)
    props = set_properties_value(PROPERTIES, content)
    return render_template(
        '/admin/content.html',
        page_data=dict(
            content_id=content_id,
            edit=True,
            article=None,
            title=PAGE_TITLE,
            back_url=ROOT_URL,
            action_url=f'{ROOT_URL}/edit/{content_id}',
            properties=props,
            blocks_url=f'/admin/blocks/{content_id}',
            content_type=RESOURCE_TYPE,
        )
    )


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/create', methods=['POST'])
@login_required()
def create_action() -> Any:
    """
    Insert content to database.
    """
    try:
        data = request.form.to_dict()
        content_id = content_service.insert(data)
        flash('Content created successfully!', category='success')
        return redirect(f'{ROOT_URL}/edit/{content_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route('/edit/<content_id>', methods=['POST'])
@login_required()
def edit_action(content_id: int) -> Any:
    """
    Update content in database.
    """
    try:
        data = request.form.to_dict()
        content_service.update(content_id, data)
        flash('Content updated successfully!', category='success')
        return redirect(f'{ROOT_URL}/edit/{content_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route('/delete/<content_id>', methods=['GET'])
@login_required()
def delete_action(content_id: int) -> Any:
    """
    Delete content from database.
    """
    try:
        content_service.delete(content_id)
        flash('Content sent to trash bin!', category='success')
        return redirect(ROOT_URL)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route('/duplicate/<content_id>/<context>',
                 methods=['GET'])
@login_required()
def duplicate_action(content_id: int, context: str) -> Any:
    """
    Duplicate content.
    """
    try:
        content_service.duplicate(content_id, context)
        flash('Content duplicated successfully!', category='success')
        return redirect(ROOT_URL)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)

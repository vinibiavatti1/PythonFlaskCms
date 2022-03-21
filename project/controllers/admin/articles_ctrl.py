"""
Articles controller.
"""
from typing import Any
from werkzeug.utils import redirect
from flask import Blueprint, request, render_template, flash, abort
from project.models.property_model import PropertyModel
from project.services import content_service
from project.enums import resource_type_enum
from project.decorators.security_decorators import login_required
from project.properties.article_properties import article_properties
from project.utils.data_utils import set_properties_value
from project.utils.ctrl_utils import get_admin_list_url
from project.decorators.context_decorators import process_context


# Controller properties
CONTROLLER_NAME = 'admin_articles_ctrl'
URL_PREFIX = '/<context>/admin/articles'

PAGE_TITLE = 'Articles'
LIST_NAME = 'articles'
RESOURCE_TYPE = resource_type_enum.ARTICLE
PROPERTIES = article_properties


# Blueprint
blueprint = Blueprint(
    CONTROLLER_NAME,
    __name__,
    url_prefix=URL_PREFIX
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
        'Private',
        'Published',
        'Created On',
        'Actions',
    ]
    data: list[Any] = list()
    contents = content_service.select_all(context, RESOURCE_TYPE)
    for content in contents:
        id_ = content['id']
        data.append((
            id_,
            content['name'],
            'True' if content['private'] == 1 else 'False',
            'True' if content['published'] == 1 else 'False',
            content['created_on'],
            f'<a href="{list_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/datatable.html',
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
def create_view(context: str) -> str:
    """
    Render create page.
    """
    list_url = get_admin_list_url(context, LIST_NAME)
    return render_template(
        '/admin/content.html',
        page_data=dict(
            context=context,
            content_id=None,
            edit=False,
            title=PAGE_TITLE,
            root_url=list_url,
            properties=PROPERTIES,
            resource_type=RESOURCE_TYPE,
        )
    )


@blueprint.route('/edit/<content_id>', methods=['GET'])
@login_required()
@process_context()
def edit_view(context: str, content_id: int) -> str:
    """
    Render edit page.
    """
    list_url = get_admin_list_url(context, LIST_NAME)
    content = content_service.select_by_id(context, content_id)
    if not content:
        abort(404)
    props = set_properties_value(PROPERTIES, content)
    return render_template(
        '/admin/content.html',
        page_data=dict(
            context=context,
            content_id=content_id,
            edit=True,
            title=PAGE_TITLE,
            root_url=list_url,
            properties=props,
            resource_type=RESOURCE_TYPE,
        )
    )


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/create', methods=['POST'])
@login_required()
@process_context()
def create_action(context: str) -> Any:
    """
    Insert content to database.
    """
    list_url = get_admin_list_url(context, LIST_NAME)
    try:
        data = request.form.to_dict()
        content_id = content_service.insert(context, data)
        flash('Content created successfully!', category='success')
        return redirect(f'{list_url}/edit/{content_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route('/edit/<content_id>', methods=['POST'])
@login_required()
@process_context()
def edit_action(context: str, content_id: int) -> Any:
    """
    Update content in database.
    """
    list_url = get_admin_list_url(context, LIST_NAME)
    try:
        data = request.form.to_dict()
        content_service.update(context, content_id, data)
        flash('Content updated successfully!', category='success')
        return redirect(f'{list_url}/edit/{content_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route('/delete/<content_id>', methods=['GET'])
@login_required()
@process_context()
def delete_action(context: str, content_id: int) -> Any:
    """
    Delete content from database.
    """
    list_url = get_admin_list_url(context, LIST_NAME)
    try:
        content_service.delete(context, content_id)
        flash('Content sent to trash bin!', category='success')
        return redirect(list_url)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route('/duplicate/<content_id>/<to_context>',
                 methods=['GET'])
@login_required()
@process_context()
def duplicate_action(context: str, content_id: int, to_context: str) -> Any:
    """
    Duplicate content.
    """
    list_url = get_admin_list_url(context, LIST_NAME)
    try:
        content_service.duplicate(context, content_id, to_context)
        flash('Content duplicated successfully!', category='success')
        return redirect(list_url)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)

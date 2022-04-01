"""
Object controller.
"""
from typing import Any, Optional
from flask import Blueprint, request, abort, render_template, flash, redirect
from project.enums import object_type_enum
from project.decorators.security_decorators import login_required
from project.decorators.record_decorators import validate_content_type
from project.services import history_service
from project.utils import record_utils
from project.utils.data_utils import set_properties_value
from project.utils.ctrl_utils import get_admin_list_url
from project.entities.object_entity import ObjectEntity
from project.services import object_service
from project.decorators.context_decorators import process_context
from project.processors import content_ctrl_processor
from project.records.content_type_records import content_type_records
from project.records.page_type_records import page_type_records
from project.records.resource_type_records import resource_type_records


# Blueprint data
blueprint = Blueprint(
    name='admin_object_ctrl',
    import_name=__name__,
    url_prefix='/<context>/admin/object'
)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/contents', methods=['GET'])
@login_required()
@process_context()
def list_contents_view(context: str) -> Any:
    """
    List content view endpoint.
    """
    list_url = get_admin_list_url(context, object_type_enum.CONTENT)
    headers = [
        '#',
        'Name',
        'Type',
        'Private',
        'Published',
        'Created On',
        'Actions',
    ]
    data: list[Any] = list()
    objects = object_service.select_by_type(context, object_type_enum.CONTENT)
    for entity in objects:
        id_ = entity.id
        private = entity.properties['private'] == '1'
        published = entity.properties['published'] == '1'
        subtype = record_utils.get_record_by_name(
            entity.object_subtype, content_type_records
        )
        icon = getattr(subtype, "icon")
        label = getattr(subtype, "label")
        data.append((
            id_,
            entity.name,
            f'<i class="bi {icon}"></i> {label}',
            'True' if private == '1' else 'False',
            '<i class="bi bi-broadcast"></i> True' if published else 'False',
            entity.created_on,
            f'<a href="{list_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/content_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            title=object_type_enum.CONTENT.title(),
            btn_link=f'{list_url}/create',
        )
    )


@blueprint.route('/pages', methods=['GET'])
@login_required()
@process_context()
def list_pages_view(context: str) -> Any:
    """
    List page view endpoint.
    """
    list_url = get_admin_list_url(context, object_type_enum.PAGE)
    headers = [
        '#',
        'Name',
        'Type',
        'Private',
        'Published',
        'Created On',
        'Actions',
    ]
    data: list[Any] = list()
    objects = object_service.select_by_type(context, object_type_enum.PAGE)
    for entity in objects:
        id_ = entity.id
        private = entity.properties['private'] == '1'
        published = entity.properties['published'] == '1'
        subtype = record_utils.get_record_by_name(
            entity.object_subtype, page_type_records
        )
        icon = getattr(subtype, "icon")
        label = getattr(subtype, "label")
        data.append((
            id_,
            entity.name,
            f'<i class="bi {icon}"></i> {label}',
            'True' if private == '1' else 'False',
            '<i class="bi bi-broadcast"></i> True' if published else 'False',
            entity.created_on,
            f'<a href="{list_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/content_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            title=object_type_enum.PAGE.title(),
            btn_link=f'{list_url}/create',
        )
    )


@blueprint.route('/resources', methods=['GET'])
@login_required()
@process_context()
def list_resources_view(context: str) -> Any:
    """
    List resource view endpoint.
    """
    list_url = get_admin_list_url(context, object_type_enum.RESOURCE)
    headers = [
        '#',
        'Name',
        'Type',
        'Active',
        'Created On',
        'Actions',
    ]
    data: list[Any] = list()
    objects = object_service.select_by_type(context, object_type_enum.RESOURCE)
    for entity in objects:
        id_ = entity.id
        active = entity.properties['active'] == '1'
        subtype = record_utils.get_record_by_name(
            entity.object_subtype, resource_type_records
        )
        icon = getattr(subtype, "icon")
        label = getattr(subtype, "label")
        data.append((
            id_,
            entity.name,
            f'<i class="bi {icon}"></i> {label}'
            '<i class="bi bi-broadcast"></i> True' if active else 'False',
            entity.created_on,
            f'<a href="{list_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/content_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            title=object_type_enum.RESOURCE.title(),
            btn_link=f'{list_url}/create',
        )
    )







@blueprint.route('/create', methods=['GET'])
@login_required()
@process_context()
@validate_content_type()
def create_view(context: str, content_type: str) -> Any:
    """
    Render create page.
    """
    content_record = record_utils.get_content_record(content_type)
    list_url = get_admin_list_url(context, content_type)
    return render_template(
        '/admin/content.html',
        page_data=dict(
            context=context,
            content_id=None,
            edit=False,
            title=content_type.title(),
            root_url=list_url,
            properties=content_record.properties,
            resource_type=content_type,
        )
    )


@blueprint.route('/edit/<content_id>', methods=['GET'])
@login_required()
@process_context()
@validate_content_type()
def edit_view(context: str, content_type: str, content_id: int) -> Any:
    """
    Render edit page.
    """
    content_record = record_utils.get_content_record(content_type)
    list_url = get_admin_list_url(context, content_type)
    content = object_service.select_by_id(content_id)
    if not content:
        return abort(404)
    props = set_properties_value(content_record.properties, content)
    history = history_service.select_by_resource(content_id, content_type)
    return render_template(
        '/admin/content.html',
        page_data=dict(
            context=context,
            content_id=content_id,
            edit=True,
            title=content_type.title(),
            root_url=list_url,
            properties=props,
            resource_type=content_type,
            history=history,
            name=content.name,
        )
    )


@blueprint.route('/create', methods=['POST'])
@login_required()
@process_context()
@validate_content_type()
def create_action(context: str, content_type: str) -> Any:
    """
    Insert content to database.
    """
    data = request.form.to_dict()
    list_url = get_admin_list_url(context, content_type)
    content = ObjectEntity(
        context=context,
        name=data['name'],
        properties=data,
        object_subtype=content_type,
    )
    try:
        content_id = object_service.insert(content)
        flash('Content created successfully!', category='success')
        return redirect(f'{list_url}/edit/{content_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route('/edit/<content_id>', methods=['POST'])
@login_required()
@process_context()
@validate_content_type()
def edit_action(context: str, content_type: str, content_id: int) -> Any:
    """
    Update content in database.
    """
    data = request.form.to_dict()
    list_url = get_admin_list_url(context, content_type)
    content = ObjectEntity(
        context=context,
        id=content_id,
        name=data['name'],
        properties=data,
        object_subtype=content_type,
    )
    try:
        object_service.update(content)
        flash('Content updated successfully!', category='success')
        return redirect(f'{list_url}/edit/{content_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route('/delete/<content_id>', methods=['GET'])
@login_required()
@process_context()
@validate_content_type()
def delete_action(context: str, content_type: str, content_id: int) -> Any:
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
@validate_content_type()
def duplicate_action(context: str, content_type: str, content_id: int,
                     to_context: str, new_name: str) -> Any:
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

"""
Objects controller.
"""
from typing import Any, Optional, Union
from flask import Blueprint, request, abort, render_template, flash, redirect
from project.enums import object_type_enum
from project.enums import object_subtype_enum
from project.decorators.security_decorators import login_required
from project.decorators.record_decorators import validate_content_type
from project.models.content_type_model import ContentTypeModel
from project.models.resource_type_model import ResourceTypeModel
from project.services import history_service
from project.utils import record_utils
from project.utils.data_utils import set_properties_value
from project.utils.ctrl_utils import get_object_root_url
from project.entities.object_entity import ObjectEntity
from project.services import object_service
from project.decorators.context_decorators import process_context
from project.processors import content_ctrl_processor
from project.records.content_type_records import content_type_records
from project.records.page_type_records import page_type_records
from project.records.resource_type_records import resource_type_records
from project.enums import table_enum


# Blueprint data
blueprint = Blueprint(
    name='admin_objects_ctrl',
    import_name=__name__,
    url_prefix='/<context>/admin/objects'
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route(
    rule='/content',
    methods=['GET'],
    defaults={'object_sub_type': None}
)
@blueprint.route(
    rule='/content/<object_sub_type>',
    methods=['GET']
)
@login_required()
@process_context()
def list_contents_view(context: str, object_sub_type: Optional[str] = None
                       ) -> Any:
    """
    List content view endpoint.
    """
    root_url = get_object_root_url(context, object_type_enum.CONTENT)
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
    if object_sub_type is None:
        objects = object_service.select_by_type(
            context, object_type_enum.CONTENT
        )
    else:
        objects = object_service.select_by_type_and_subtype(
            context, object_type_enum.CONTENT,
            object_sub_type,
        )
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
            f'<a href="{root_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/object_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            object_type=object_type_enum.CONTENT,
            object_sub_type=object_sub_type,
            root_url=root_url,
            object_type_records=content_type_records,
        )
    )


@blueprint.route(
    rule='/page',
    methods=['GET'],
    defaults={'object_sub_type': None}
)
@blueprint.route(
    rule='/page/<object_sub_type>',
    methods=['GET']
)
@login_required()
@process_context()
def list_pages_view(context: str, object_sub_type: Optional[str] = None
                    ) -> Any:
    """
    List page view endpoint.
    """
    root_url = get_object_root_url(context, object_type_enum.PAGE)
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
    if object_sub_type is None:
        objects = object_service.select_by_type(
            context, object_type_enum.PAGE
        )
    else:
        objects = object_service.select_by_type_and_subtype(
            context, object_type_enum.PAGE,
            object_sub_type,
        )
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
            f'<a href="{root_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/object_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            object_type=object_type_enum.PAGE,
            root_url=root_url,
            object_type_records=page_type_records,
        )
    )

@blueprint.route(
    rule='/resource',
    methods=['GET'],
    defaults={'object_sub_type': None}
)
@blueprint.route(
    rule='/resource/<object_sub_type>',
    methods=['GET']
)
@login_required()
@process_context()
def list_resources_view(context: str, object_sub_type: Optional[str] = None
                        ) -> Any:
    """
    List resource view endpoint.
    """
    root_url = get_object_root_url(context, object_type_enum.RESOURCE)
    headers = [
        '#',
        'Name',
        'Type',
        'Active',
        'Created On',
        'Actions',
    ]
    data: list[Any] = list()
    if object_sub_type is None:
        objects = object_service.select_by_type(
            context, object_type_enum.RESOURCE
        )
    else:
        objects = object_service.select_by_type_and_subtype(
            context, object_type_enum.RESOURCE,
            object_sub_type,
        )
    for entity in objects:
        id_ = entity.id
        active = entity.properties['active']
        subtype = record_utils.get_record_by_name(
            entity.object_subtype, resource_type_records
        )
        icon = getattr(subtype, "icon")
        label = getattr(subtype, "label")
        data.append((
            id_,
            entity.name,
            f'<i class="bi {icon}"></i> {label}',
            '<i class="bi bi-broadcast"></i> True' if active else 'False',
            entity.created_on,
            f'<a href="{root_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/object_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            object_type=object_type_enum.RESOURCE,
            root_url=root_url,
            object_type_records=resource_type_records,
        )
    )


@blueprint.route(
    rule='/<object_type>/<object_subtype>/create',
    methods=['GET']
)
@login_required()
@process_context()
def create_view(context: str, object_type: str, object_subtype: str) -> Any:
    """
    Render create page.
    """
    record_list: list[Any] = []
    if object_type == object_type_enum.CONTENT:
        record_list = content_type_records
    elif object_type == object_type_enum.RESOURCE:
        record_list = resource_type_records
    else:
        return abort(400)
    record_data = record_utils.get_record_by_name(
        object_subtype, record_list
    )
    list_url = get_object_root_url(context, object_type)
    return render_template(
        '/admin/object_form.html',
        page_data=dict(
            context=context,
            object_id=None,
            edit=False,
            object_type=object_type,
            object_subtype=object_subtype,
            allow_blocks=getattr(record_data, 'allow_blocks', False),
            root_url=list_url,
            properties=getattr(record_data, 'properties'),
        )
    )


@blueprint.route('/<object_type>/edit/<object_id>', methods=['GET'])
@login_required()
@process_context()
def edit_view(context: str, object_type: str, object_id: int) -> Any:
    """
    Render edit page.
    """
    record_list: list[Any] = []
    if object_type == object_type_enum.CONTENT:
        record_list = content_type_records
    elif object_type == object_type_enum.RESOURCE:
        record_list = resource_type_records
    else:
        return abort(400)
    entity = object_service.select_by_id(object_id)
    if not entity:
        return abort(400)
    record = record_utils.get_record_by_name(
        entity.object_subtype,
        record_list,
    )
    root_url = get_object_root_url(context, object_type)
    props = set_properties_value(getattr(record, 'properties'), entity)
    history = history_service.select_by_target_id(
        context, table_enum.OBJECTS, object_id,
    )
    return render_template(
        '/admin/object_form.html',
        page_data=dict(
            context=context,
            object_id=object_id,
            edit=True,
            object_type=object_type,
            object_subtype=entity.object_subtype,
            root_url=root_url,
            properties=props,
            history=history,
            name=entity.name,
        )
    )


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/create', methods=['POST'])
@login_required()
@process_context()
@validate_content_type()
def create_action(context: str, content_type: str) -> Any:
    """
    Insert content to database.
    """
    data = request.form.to_dict()
    list_url = get_object_root_url(context, content_type)
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
    list_url = get_object_root_url(context, content_type)
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

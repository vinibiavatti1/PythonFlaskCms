"""
Objects controller.
"""
from typing import Any, Optional
from flask import Blueprint, request, abort, render_template, flash, redirect
from project.decorators.security_decorators import login_required
from project.decorators.context_decorators import process_context
from project.entities.object_entity import ObjectEntity
from project.records.content_type_records import content_type_records
from project.records.page_type_records import page_type_records
from project.records.resource_type_records import resource_type_records
from project.records.component_type_records import component_type_records
from project.utils import record_utils
from project.utils.data_utils import set_properties_value
from project.utils.ctrl_utils import generate_admin_url
from project.utils import str_utils
from project.services import history_service
from project.services import object_service
from project.enums import object_type_enum
from project.enums import string_types_enum as str_type
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
    object_type = object_type_enum.CONTENT
    root_url = generate_admin_url(context, 'objects', object_type)
    headers = [
        '#',
        'Type',
        'Name',
        'Private',
        'Published',
        'Created On',
        'Actions',
    ]
    data: list[Any] = list()
    if object_sub_type is None:
        objects = object_service.select_by_type(
            context, object_type
        )
    else:
        objects = object_service.select_by_type_and_subtype(
            context, object_type, object_sub_type,
        )
    for entity in objects:
        id_ = entity.id
        private = entity.properties['private'] == str_type.TRUE
        published = entity.properties['published'] == str_type.TRUE
        subtype = record_utils.get_record_by_name(
            entity.object_subtype, content_type_records
        )
        if not subtype:
            return abort(400)
        data.append((
            id_,
            f'<i class="bi {subtype.icon}"></i> {subtype.label}',
            entity.name,
            'True' if private else 'False',
            '<i class="bi bi-broadcast"></i> True' if published else 'False',
            entity.created_on,
            f'<a href="{root_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/object_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            object_type=object_type,
            object_sub_type=object_sub_type,
            title=str_utils.title(object_type, plural=True),
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
    object_type = object_type_enum.PAGE
    root_url = generate_admin_url(context, 'objects', object_type)
    headers = [
        '#',
        'Type',
        'Name',
        'Private',
        'Published',
        'Actions',
    ]
    data: list[Any] = list()
    if object_sub_type is None:
        objects = object_service.select_by_type(
            context, object_type
        )
    else:
        objects = object_service.select_by_type_and_subtype(
            context, object_type, object_sub_type,
        )
    for entity in objects:
        id_ = entity.id
        private = entity.properties['private'] == str_type.TRUE
        published = entity.properties['published'] == str_type.TRUE
        subtype = record_utils.get_record_by_name(
            entity.object_subtype, page_type_records
        )
        if not subtype:
            return abort(400)
        data.append((
            id_,
            f'<i class="bi {subtype.icon}"></i> {subtype.label}',
            entity.name,
            'True' if private else 'False',
            '<i class="bi bi-broadcast"></i> True' if published else 'False',
            f'<a href="{root_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/object_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            object_type=object_type,
            object_sub_type=object_sub_type,
            title=str_utils.title(object_type, plural=True),
            hide_new_action=True,
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
    object_type = object_type_enum.RESOURCE
    root_url = generate_admin_url(context, 'objects', object_type)
    headers = [
        '#',
        'Type',
        'Name',
        'Active',
        'Created On',
        'Actions',
    ]
    data: list[Any] = list()
    if object_sub_type is None:
        objects = object_service.select_by_type(
            context, object_type
        )
    else:
        objects = object_service.select_by_type_and_subtype(
            context, object_type, object_sub_type,
        )
    for entity in objects:
        id_ = entity.id
        active = entity.properties['active'] == str_type.TRUE
        subtype = record_utils.get_record_by_name(
            entity.object_subtype, resource_type_records
        )
        if not subtype:
            return abort(400)
        data.append((
            id_,
            f'<i class="bi {subtype.icon}"></i> {subtype.label}',
            entity.name,
            '<i class="bi bi-broadcast"></i> True' if active else 'False',
            entity.created_on,
            f'<a href="{root_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/object_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            object_type=object_type,
            object_sub_type=object_sub_type,
            title=str_utils.title(object_type, plural=True),
            root_url=root_url,
            object_type_records=resource_type_records,
        )
    )


@blueprint.route(
    rule='/component',
    methods=['GET'],
    defaults={'object_sub_type': None}
)
@blueprint.route(
    rule='/component/<object_sub_type>',
    methods=['GET']
)
@login_required()
@process_context()
def list_components_view(context: str, object_sub_type: Optional[str] = None
                    ) -> Any:
    """
    List component view endpoint.
    """
    object_type = object_type_enum.COMPONENT
    root_url = generate_admin_url(context, 'objects', object_type)
    headers = [
        '#',
        'Type',
        'Name',
        'Actions',
    ]
    data: list[Any] = list()
    if object_sub_type is None:
        objects = object_service.select_by_type(
            context, object_type
        )
    else:
        objects = object_service.select_by_type_and_subtype(
            context, object_type, object_sub_type,
        )
    for entity in objects:
        id_ = entity.id
        subtype = record_utils.get_record_by_name(
            entity.object_subtype, component_type_records
        )
        if not subtype:
            return abort(400)
        data.append((
            id_,
            f'<i class="bi {subtype.icon}"></i> {subtype.label}',
            entity.name,
            f'<a href="{root_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/object_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            object_type=object_type,
            object_sub_type=object_sub_type,
            title=str_utils.title(object_type, plural=True),
            hide_new_action=True,
            root_url=root_url,
            object_type_records=component_type_records,
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
    record_list = record_utils.get_record_list_by_object_type(object_type)
    if not record_list:
        return abort(400)

    record = record_utils.get_record_by_name(object_subtype, record_list)
    if not record:
        return abort(400)

    root_url = generate_admin_url(
        context, 'objects', object_type
    )
    action_url = generate_admin_url(
        context, 'objects', object_type, object_subtype, 'create',
    )
    return render_template(
        '/admin/object_form.html',
        page_data=dict(
            context=context,
            object_id=None,
            edit=False,
            object_type=object_type,
            object_subtype=object_subtype,
            title=str_utils.title(object_subtype),
            root_url=root_url,
            action_url=action_url,
            properties=getattr(record, 'properties'),
            allow_duplicated=record.allow_duplicated,
            allow_deleted=record.allow_deleted,
        )
    )


@blueprint.route(
    rule='/<object_type>/edit/<object_id>',
    methods=['GET']
)
@login_required()
@process_context()
def edit_view(context: str, object_type: str, object_id: int) -> Any:
    """
    Render edit page.
    """
    record_list = record_utils.get_record_list_by_object_type(object_type)
    if not record_list:
        return abort(400)

    entity = object_service.select_by_id(object_id)
    if not entity:
        return abort(400)

    object_subtype = entity.object_subtype
    record = record_utils.get_record_by_name(
        object_subtype,
        record_list,
    )
    if not record:
        return abort(400)

    root_url = generate_admin_url(
        context, 'objects', object_type,
    )
    action_url = generate_admin_url(
        context, 'objects', object_type, object_subtype, 'edit', str(object_id)
    )
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
            object_subtype=object_subtype,
            title=str_utils.title(object_subtype),
            root_url=root_url,
            action_url=action_url,
            properties=props,
            history=history,
            name=entity.name,
            allow_duplicated=record.allow_duplicated,
            allow_deleted=record.allow_deleted,
            nested_objects=record.nested_objects,
        )
    )


###############################################################################
# Action Routes
###############################################################################


@blueprint.route(
    rule='/<object_type>/<object_subtype>/create',
    methods=['POST']
)
@login_required()
@process_context()
def create_action(context: str, object_type: str, object_subtype: str) -> Any:
    """
    Insert content to database.
    """
    data = request.form.to_dict()
    root_url = generate_admin_url(
        context, 'objects', object_type,
    )
    new_object = ObjectEntity(
        context=context,
        name=data['name'],
        properties=data,
        object_type=object_type,
        object_subtype=object_subtype,
    )
    try:
        entity_id = object_service.insert(new_object)
        flash('Content created successfully!', category='success')
        return redirect(f'{root_url}/edit/{entity_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route(
    rule='/<object_type>/<object_subtype>/edit/<object_id>',
    methods=['POST']
)
@login_required()
@process_context()
def edit_action(context: str, object_type: str, object_subtype: str,
                object_id: int) -> Any:
    """
    Update content in database.
    """
    data = request.form.to_dict()
    root_url = generate_admin_url(
        context, 'objects', object_type,
    )
    edit_object = ObjectEntity(
        context=context,
        id=object_id,
        name=data['name'],
        properties=data,
        object_type=object_type,
        object_subtype=object_subtype,
    )
    try:
        object_service.update(edit_object)
        flash('Content updated successfully!', category='success')
        return redirect(f'{root_url}/edit/{object_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route(
    rule='/<object_type>/delete/<object_id>',
    methods=['GET']
)
@login_required()
@process_context()
def delete_action(context: str, object_type: str, object_id: int) -> Any:
    """
    Delete content from database.
    """
    root_url = generate_admin_url(
        context, 'objects', object_type,
    )
    try:
        object_service.delete(object_id)
        flash(f'Content {object_id} sent to trash bin', category='success')
        return redirect(root_url)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route(
    rule='/<object_type>/duplicate/<object_id>/<to_context>/<new_name>',
    methods=['GET']
)
@login_required()
@process_context()
def duplicate_action(context: str, object_type: str, object_id: int,
                     to_context: str, new_name: str) -> Any:
    """
    Duplicate content.
    """
    root_url = generate_admin_url(
        context, 'objects', object_type,
    )
    try:
        object_service.duplicate(object_id, to_context, new_name)
        flash('Content duplicated successfully!', category='success')
        return redirect(root_url)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


###############################################################################
# Ajax Routes
###############################################################################


@blueprint.route(
    rule='/exists/<object_type>/<object_subtype>/<name>',
    methods=['GET']
)
@login_required()
def object_exists(context: str, object_type: str, object_subtype: str,
                  name: str) -> Any:
    """
    Verify if object exists.
    """
    exists = object_service.object_exists(
        context, object_type, object_subtype, name
    )
    return dict(exists=exists)

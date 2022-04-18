"""
Objects controller.
"""
from typing import Any, Optional
from flask import Blueprint, request, abort, render_template, flash, redirect
from project.decorators.security_decorators import login_required
from project.decorators.context_decorators import process_context
from project.entities.object_entity import ObjectEntity
from project.models.object_model import ObjectModel
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
from project.enums import object_enum
from project.enums import string_types_enum as str_type
from project.enums import table_enum
import json


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
    rule='/',
    methods=['GET'],
    defaults={'object_name': None}
)
@blueprint.route(
    rule='/<object_name>',
    methods=['GET']
)
@login_required()
@process_context()
def list_objects_view(context: str, object_name: Optional[str] = None
                       ) -> Any:
    """
    List content view endpoint.
    """
    root_url = generate_admin_url(context, 'objects')
    back_url = generate_admin_url(
        context, 'objects'
    )
    change_order_url = generate_admin_url(
        context, 'objects', 'change_order', object_name if object_name else '',
    )
    referrer_url = request.referrer
    headers = [
        '#',
        'Name',
        'Type',
        'Published',
        'Created On',
        'Edit',
        'Children',
    ]
    objects: list[ObjectEntity] = list()
    children: list[ObjectModel] = list()
    data: list[Any] = list()
    title = 'Root'
    parent_name = None

    # Get record and data
    if object_name is not None:
        entity = object_service.select_by_name(context, object_name)
        if not entity:
            return abort(400)
        record = record_utils.get_record_by_name(entity.object_type)
        if not record:
            return abort(400)
        if entity.reference_id:
            parent = object_service.select_by_id(entity.reference_id)
            if not parent:
                return abort(400)
            parent_name = parent.name
            back_url = generate_admin_url(
                context, 'objects', parent.name,
            )
        title = entity.name
        children = record_utils.get_records_by_names(record.children)
        objects = object_service.select_by_reference(entity.id)
    else:
        children = record_utils.get_root_records()
        objects = object_service.select_root_objects(context)

    # Filter children
    children = [child for child in children if child.allow_actions]

    # Parse entities
    for entity in objects:
        id_ = entity.id
        published = entity.properties.get('published', '1') == str_type.TRUE
        object_type = record_utils.get_record_by_name(
            entity.object_type
        )
        if not object_type:
            continue
        data.append((
            entity.object_order,
            f'<i class="bi {object_type.icon}"></i> '
            f'{entity.name}',
            f'{object_type.name}',
            f'<i class="bi bi-broadcast"></i> True' if published else 'False',
            entity.created_on,
            f'<i class="bi bi-pencil"></i> '
            f'<a href="{root_url}/edit/{id_}">Edit</a>',
            f'<i class="bi bi-folder2-open"></i> '
            f'<a href="{root_url}/{entity.name}">Children</a>'
        ))

    # Render template
    return render_template(
        '/admin/object_list.html',
        page_data=dict(
            object_name=object_name,
            headers=headers,
            data=data,
            referrer_url=referrer_url,
            title=title,
            children=children,
            back_url=back_url,
            parent_name=parent_name,
            change_order_url=change_order_url,
        )
    )


@blueprint.route(
    rule='/change_order',
    methods=['GET'],
    defaults={'object_name': None}
)
@blueprint.route(
    rule='/change_order/<object_name>',
    methods=['GET']
)
@login_required()
@process_context()
def change_order_view(context: str, object_name: Optional[str] = None
                      ) -> Any:
    """
    Change order view endpoint.
    """
    back_url = generate_admin_url(
        context, 'objects'
    )
    action_url = generate_admin_url(
        context, 'objects', 'save_order'
    )
    referrer_url = request.referrer
    objects: list[ObjectEntity] = list()
    data: list[Any] = list()
    title = 'Root'

    # Get record and data
    if object_name is not None:
        entity = object_service.select_by_name(context, object_name)
        if not entity:
            return abort(400)
        record = record_utils.get_record_by_name(entity.object_type)
        if not record:
            return abort(400)
        if entity.reference_id:
            parent = object_service.select_by_id(entity.reference_id)
            if not parent:
                return abort(400)
            back_url = generate_admin_url(
                context, 'objects', parent.name,
            )
        title = entity.name
        objects = object_service.select_by_reference(entity.id)
    else:
        objects = object_service.select_root_objects(context)

    # Parse entities
    for entity in objects:
        object_type = record_utils.get_record_by_name(
            entity.object_type
        )
        if not object_type:
            continue
        data.append({
            "id": entity.id,
            "order": entity.object_order,
            "name": f'<i class="bi {object_type.icon}"></i> {entity.name}',
            "type": object_type.name
        })

    # Render template
    return render_template(
        '/admin/object_order_list.html',
        page_data=dict(
            object_name=object_name,
            data=data,
            referrer_url=referrer_url,
            title=title,
            back_url=back_url,
            action_url=action_url,
        )
    )


@blueprint.route(
    rule='/<object_type>/create',
    methods=['GET'],
    defaults={'reference_id': None}
)
@blueprint.route(
    rule='/<object_type>/create/<reference_id>',
    methods=['GET']
)
@login_required()
@process_context()
def create_view(context: str, object_type: str,
                reference_id: Optional[str] = None) -> Any:
    """
    Render create page.
    """
    record = record_utils.get_record_by_name(object_type)
    referrer_url = request.referrer
    if not record:
        return abort(400)

    back_url = generate_admin_url(
        context, 'objects'
    )
    if reference_id:
        parent = object_service.select_by_id(int(reference_id))
        if parent:
            back_url = generate_admin_url(
                context, 'objects', parent.name
            )

    action_url = generate_admin_url(
        context, 'objects', 'create', reference_id if reference_id else ''
    )
    return render_template(
        '/admin/object_form.html',
        page_data=dict(
            context=context,
            object_id=None,
            edit=False,
            object_type=object_type,
            title=object_type,
            action_url=action_url,
            back_url=back_url,
            properties=record.properties,
            allow_actions=record.allow_actions,
            referrer_url=referrer_url,
            reference_id=reference_id,
        )
    )


@blueprint.route(
    rule='/edit/<object_id>',
    methods=['GET']
)
@login_required()
@process_context()
def edit_view(context: str, object_id: int) -> Any:
    """
    Render edit page.
    """
    # Get entity and record
    entity = object_service.select_by_id(object_id)
    if not entity:
        return abort(400)

    record = record_utils.get_record_by_name(entity.object_type)
    if not record:
        return abort(400)

    # Back URL
    back_url = generate_admin_url(
        context, 'objects',
    )
    if entity.reference_id:
        parent = object_service.select_by_id(entity.reference_id)
        if parent:
            back_url = generate_admin_url(
                context, 'objects', parent.name
            )
    action_url = generate_admin_url(
        context, 'objects', entity.object_type, 'edit', str(object_id)
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
            object_type=entity.object_type,
            title=entity.object_type,
            back_url=back_url,
            action_url=action_url,
            properties=props,
            history=history,
            name=entity.name,
            allow_actions=record.allow_actions,
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


@blueprint.route(
    rule='/save_order',
    methods=['POST']
)
@login_required()
@process_context()
def save_order_action(context: str) -> Any:
    """
    Save order endpoint.
    """
    data = request.form.to_dict()
    json_data: list[dict[str, Any]] = json.loads(data['json_data'])
    try:
        for item in json_data:
            object_service.update_order(
                int(item['id']), int(item['object_order'])
            )
        flash('Order updated successfully!', category='success')
        return redirect(data['back_url'])
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

"""
Content controller processor.

Wrapper to process content controller endpoints with default pre-implemented
routines.
"""
from typing import Any
from werkzeug.utils import redirect
from flask import request, render_template, flash, abort
from project.entities.object_entity import ObjectEntity
from project.services import history_service, object_service
from project.utils.data_utils import set_properties_value
from project.utils.ctrl_utils import get_object_root_url


def process_list_view(context: str, resource_type: str, list_name: str,
                      title: str) -> Any:
    """
    List view wrapper.
    """
    list_url = get_object_root_url(context, list_name)
    headers = [
        '#',
        'Name',
        'Private',
        'Published',
        'Created On',
        'Actions',
    ]
    data: list[Any] = list()
    contents = object_service.select_all_by_type(context, resource_type)
    for content in contents:
        id_ = content.id
        private = content.properties['private'] == '1'
        published = content.properties['published'] == '1'
        data.append((
            id_,
            content.name,
            'True' if private == '1' else 'False',
            '<i class="bi bi-broadcast"></i> True' if published else 'False',
            content.created_on,
            f'<a href="{list_url}/edit/{id_}">Details</a>'
        ))
    return render_template(
        '/admin/content_list.html',
        page_data=dict(
            headers=headers,
            data=data,
            title=title,
            btn_link=f'{list_url}/create',
        )
    )


def process_create_view(context: str, resource_type: str, list_name: str,
                        title: str, properties: list[Any]) -> Any:
    """
    Create view wrapper.
    """
    list_url = get_object_root_url(context, list_name)
    return render_template(
        '/admin/content.html',
        page_data=dict(
            context=context,
            content_id=None,
            edit=False,
            title=title,
            root_url=list_url,
            properties=properties,
            resource_type=resource_type,
        )
    )


def process_edit_view(context: str, resource_type: str, list_name: str,
                      title: str, properties: list[Any],
                      content_id: int) -> Any:
    """
    Edit view wrapper.
    """
    list_url = get_object_root_url(context, list_name)
    content = object_service.select_by_id(content_id)
    if not content:
        return abort(404)
    props = set_properties_value(properties, content)
    history = history_service.select_by_resource(content_id, resource_type)
    return render_template(
        '/admin/content.html',
        page_data=dict(
            context=context,
            content_id=content_id,
            edit=True,
            title=title,
            root_url=list_url,
            properties=props,
            resource_type=resource_type,
            history=history,
            name=content.name,
        )
    )


def process_create_action(context: str, resource_type: str,
                          data: dict[str, Any], list_name: str) -> Any:
    """
    Create action wrapper.
    """
    list_url = get_object_root_url(context, list_name)
    content = ObjectEntity(
        context=context,
        name=data['name'],
        properties=data,
        object_subtype=resource_type,
    )
    try:
        content_id = object_service.insert(content)
        flash('Content created successfully!', category='success')
        return redirect(f'{list_url}/edit/{content_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


def process_edit_action(context: str, resource_type: str, data: dict[str, Any],
                        list_name: str, content_id: int) -> Any:
    """
    Edit action wrapper.
    """
    list_url = get_object_root_url(context, list_name)
    content = ObjectEntity(
        context=context,
        id=content_id,
        name=data['name'],
        properties=data,
        object_subtype=resource_type,
    )
    try:
        object_service.update(content)
        flash('Content updated successfully!', category='success')
        return redirect(f'{list_url}/edit/{content_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


def process_delete_action(context: str, list_name: str, content_id: int
                          ) -> Any:
    """
    Delete action wrapper.
    """
    list_url = get_object_root_url(context, list_name)
    try:
        object_service.delete(content_id)
        flash(f'Content {content_id} sent to trash bin', category='success')
        return redirect(list_url)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


def process_duplicate_action(context: str, list_name: str, content_id: int,
                             to_context: str, new_name: str) -> Any:
    """
    Duplicate action wrapper.
    """
    list_url = get_object_root_url(context, list_name)
    try:
        object_service.duplicate(content_id, to_context, new_name)
        flash('Content duplicated successfully!', category='success')
        return redirect(list_url)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)

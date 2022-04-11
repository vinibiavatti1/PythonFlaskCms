"""
Import/Export controller.
"""
from typing import Any
from flask import Blueprint, request, abort, render_template, flash, \
    redirect,  Response
from project.decorators.security_decorators import login_required
from project.decorators.context_decorators import process_context
from project.records.content_type_records import content_type_records
from project.records.page_type_records import page_type_records
from project.records.resource_type_records import resource_type_records
from project.services import import_export_service


# Blueprint data
blueprint = Blueprint(
    name='admin_import_export_ctrl',
    import_name=__name__,
    url_prefix='/<context>/admin/import_export'
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route(
    rule='/',
    methods=['GET']
)
@login_required()
@process_context()
def import_export_view(context: str) -> Any:
    """
    Import/Export view.
    """
    content_types = [e.name for e in content_type_records]
    page_types = [e.name for e in page_type_records]
    resource_types = [e.name for e in resource_type_records]
    return render_template(
        '/admin/import_export.html',
        page_data=dict(
            context=context,
            content_types=content_types,
            page_types=page_types,
            resource_types=resource_types,
        )
    )


###############################################################################
# Action Routes
###############################################################################


@blueprint.route(
    rule='/export',
    methods=['POST'],
)
@login_required()
@process_context()
def export_action(context: str) -> Any:
    """
    Import/Export view.
    """
    data = request.form.to_dict()
    datatype = data['datatype']
    object_type = data['object_type']
    object_subtype = data['object_subtype']
    component_type = data['component_type']
    if datatype == 'objects':
        json = import_export_service.export_objects(
            None if object_type == 'all' else object_type,
            None if object_subtype == 'all' else object_subtype,
        )
    elif datatype == 'components':
        json = import_export_service.export_component(
            None if component_type == 'all' else component_type,
        )
    elif datatype == 'properties':
        json = import_export_service.export_properties()
    elif datatype == 'users':
        json = import_export_service.export_users()
    elif datatype == 'files':
        json = import_export_service.export_files()
    else:
        flash(f'Invalid datatype: {datatype}', category='danger')
        return redirect(request.referrer)
    return Response(
        json,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment;filename=export.json"}
    )

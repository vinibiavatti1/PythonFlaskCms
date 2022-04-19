"""
Import/Export controller.
"""
from datetime import datetime
from typing import Any
from flask import Blueprint, request, abort, render_template, flash, \
    redirect,  Response, current_app
from project.decorators.security_decorators import login_required
from project.decorators.context_decorators import process_context
from project.services import import_export_service
from project.services import object_service
from project.services import property_service
from project.utils import datetime_utils
from project.utils import ctrl_utils
import json


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
    import_action_url = ctrl_utils.generate_admin_url(
        context, 'import_export', 'import'
    )
    export_action_url = ctrl_utils.generate_admin_url(
        context, 'import_export', 'export'
    )

    # Properties
    properties = list()
    props = property_service.select_all(context)
    record: Any = None
    for prop in props:
        record = property_service.get_record_by_name(prop['name'])
        if record is None:
            continue
        properties.append({
            'id': prop['id'],
            'name': prop['name'],
            'description': record.description,
        })

    # Objects
    objects = list()
    for entity in object_service.select_all(context):
        record = object_service.get_record_by_name(entity.object_type)
        if record is None:
            continue
        objects.append({
            'id': entity.id,
            'name': entity.name,
            'object_type': entity.object_type,
            'reference_name': entity.reference_name,
            'icon': record.icon,
        })
    return render_template(
        '/admin/import_export.html',
        page_data=dict(
            context=context,
            objects=objects,
            properties=properties,
            import_action_url=import_action_url,
            export_action_url=export_action_url,
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
    try:
        data = request.form.to_dict()
        datatype = data['datatype']
        id_list = json.loads(data['id_list'])
        if datatype == 'objects':
            exports = import_export_service.export_objects_by_id_list(
                id_list
            )
        elif datatype == 'properties':
            exports = import_export_service.export_properties_by_id_list(
                id_list
            )
        elif datatype == 'users':
            exports = import_export_service.export_users()
        elif datatype == 'files':
            exports = import_export_service.export_files()
        else:
            flash(f'Invalid datatype: {datatype}', category='danger')
            return redirect(request.referrer)
        exports = datetime_utils.convert_list_datetime_to_timestamp(
            exports
        )
        current_datetime = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        filename = f'export_{datatype}_{current_datetime}.json'
        return Response(
            json.dumps(exports, indent=4),
            mimetype="text/plain",
            headers={
                "Content-Disposition": f"attachment;filename={filename}"
            }
        )
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route(
    rule='/import',
    methods=['POST'],
)
@login_required()
@process_context()
def import_action(context: str) -> Any:
    """
    Import data to database.
    """
    try:
        data = request.form.to_dict()
        datatype = data['datatype']
        json_data = data['json_data']
        import_action = data['import_action']
        if datatype == 'objects':
            import_export_service.import_objects(
                json_data, import_action
            )
        elif datatype == 'properties':
            import_export_service.import_properties(
                json_data, import_action
            )
        elif datatype == 'users':
            pass
        flash(f'Data imported successfully', category='success')
        return redirect(request.referrer)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)

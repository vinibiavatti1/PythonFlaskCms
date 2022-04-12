"""
Import/Export controller.
"""
from datetime import datetime
from typing import Any
from flask import Blueprint, request, abort, render_template, flash, \
    redirect,  Response, current_app
from project.decorators.security_decorators import login_required
from project.decorators.context_decorators import process_context
from project.records.content_type_records import content_type_records
from project.records.page_type_records import page_type_records
from project.records.resource_type_records import resource_type_records
from project.services import import_export_service
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
        object_type = data['object_type']
        object_subtype = data['object_subtype']
        component_type = data['component_type']
        if datatype == 'objects':
            data_to_export = import_export_service.export_objects(
                context,
                None if object_type == 'all' else object_type,
                None if object_subtype == 'all' else object_subtype,
            )
        elif datatype == 'components':
            data_to_export = import_export_service.export_component(
                context,
                component_type,
            )
        elif datatype == 'properties':
            data_to_export = import_export_service.export_properties(
                context
            )
        elif datatype == 'users':
            data_to_export = import_export_service.export_users()
        elif datatype == 'files':
            data_to_export = import_export_service.export_files()
        else:
            flash(f'Invalid datatype: {datatype}', category='danger')
            return redirect(request.referrer)
        data_to_export = datetime_utils.convert_list_datetime_to_timestamp(
            data_to_export
        )
        current_datetime = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        filename = f'export_{current_datetime}.json'
        return Response(
            json.dumps(data_to_export),
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
        elif datatype == 'navbar':
            pass
        elif datatype == 'footer':
            pass
        elif datatype == 'properties':
            pass
        elif datatype == 'users':
            pass
        flash(f'Data imported successfully', category='success')
        return redirect(request.referrer)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)

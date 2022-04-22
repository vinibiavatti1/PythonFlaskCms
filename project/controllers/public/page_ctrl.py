"""
Page endpoints.
"""
from typing import Any
from werkzeug.utils import redirect
from flask import Blueprint, request, render_template, flash, abort
from project.services import object_service


# Controller data
CONTROLLER_NAME = 'public_page_ctrl'


# Blueprint
blueprint = Blueprint(
    CONTROLLER_NAME,
    __name__
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/<context>/page/<page_name>', methods=['GET'])
def load_page(context: str, page_name: str) -> Any:
    """
    Render website page.
    """
    try:
        page = object_service.select_by_name(context, page_name)
        if page is None:
            return abort(404)
        record = object_service.get_record_by_name(page.object_type)
        if not record or not record.is_content:
            return abort(404)
        template_name = record.template
        children = object_service.select_by_reference(context, page_name)
        return render_template(
            f'/public/{template_name}.html',
            page_data=dict(
                context=context,
                page_name=page_name,
                children=children,
                **page.properties,
            )
        )
    except Exception as err:
        flash(str(err), category='danger')
        return abort(404)

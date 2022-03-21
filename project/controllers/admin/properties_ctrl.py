"""
Properties controller module.
"""
from typing import Any
from flask import Blueprint, render_template, flash, request, redirect
from project.models.property_model import PropertyModel
from project.decorators.security_decorators import login_required
from project.decorators.context_decorators import process_context
from project.records.property_records import property_records
from project.services import property_service


# Controller data
CONTROLLER_NAME = 'admin_properties_ctrl'
URL_PREFIX = '/<context>/admin/properties'


# Blueprint
blueprint = Blueprint(
    CONTROLLER_NAME,
    __name__,
    url_prefix=URL_PREFIX
)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@login_required()
@process_context()
def index(context: str) -> Any:
    """
    Render properties page.
    """
    db_properties = property_service.select_all(context)
    for prop in property_records:
        if isinstance(prop, PropertyModel):
            prop.value = db_properties[prop.name]
    return render_template(
        '/admin/properties.html',
        data=dict(properties=property_records),
    )


@blueprint.route('/save', methods=['POST'])
@login_required()
@process_context()
def save(context: str) -> Any:
    """
    Render properties page.
    """
    property_service.set_properties(context, request.form.to_dict())
    flash('Properties saved successfully!', category='success')
    return redirect(request.referrer)

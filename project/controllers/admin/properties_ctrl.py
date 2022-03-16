"""
Properties controller module.
"""
from typing import Any
from flask import Blueprint, render_template, flash, request, redirect, url_for
from project.models.property_model import PropertyModel
from project.decorators.security_decorators import login_required
from project.records.properties import properties
from project.services import property_service


# Blueprint
blueprint = Blueprint('properties', __name__, url_prefix='/admin/properties')


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    """
    Render properties page.
    """
    db_properties = property_service.select_all()
    for prop in properties:
        if isinstance(prop, PropertyModel):
            prop.value = db_properties[prop.name]
    return render_template(
        '/admin/properties.html',
        data=dict(properties=properties),
    )


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/save', methods=['POST'])
@login_required()
def save() -> Any:
    """
    Render properties page.
    """
    property_service.set_properties(request.form.to_dict())
    flash('Properties saved successfully!', category='success')
    return redirect(url_for('.index'))

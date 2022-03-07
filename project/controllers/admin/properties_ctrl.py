from flask import Blueprint, render_template
from project.utils.security_utils import login_required
from project.registry.properties import properties


# Blueprint
blueprint = Blueprint('properties', __name__, url_prefix='/admin/properties')


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    return render_template(
        '/admin/properties.html',
        properties=properties,
    )

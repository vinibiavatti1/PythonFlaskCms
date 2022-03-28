from flask import Blueprint, render_template
from project.decorators.security_decorators import login_required


# Blueprint
blueprint = Blueprint(
    'admin_form_ctrl',
    __name__,
    url_prefix='/admin/form'
)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    return render_template('/admin/form.html', data={})

"""
Information Controller.

This module provide the routes for information.
"""
from flask import Blueprint, render_template
from project.decorators.security_decorators import login_required


# Blueprint
blueprint = Blueprint(
    'admin_information_ctrl',
    __name__,
    url_prefix='/admin/information'
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    """
    Index route to information view.
    """
    return render_template(
        '/admin/information.html',
        data={}
    )

"""
Admin auth endpoints.
"""
from typing import Any
from werkzeug.utils import redirect
from flask import Blueprint, request, render_template, flash
from project.validators import auth_validator
from project.services import auth_service


# Controller data
CONTROLLER_NAME = 'admin_auth_ctrl'
INITIAL_PAGE = '/objects'


# Blueprint
blueprint = Blueprint(
    CONTROLLER_NAME,
    __name__
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/admin', methods=['GET'])
def login() -> str:
    """
    Render login page route.
    """
    return render_template('/admin/login.html')


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/admin/login', methods=['POST'])
def login_action() -> Any:
    """
    Login action route.
    """
    try:
        login_data = request.form.to_dict()
        auth_validator.validate_login_data(login_data)
        context = login_data['context']
        auth_service.process_login(context, login_data)
        context = login_data['context']
        return redirect(f'/{context}/admin{INITIAL_PAGE}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect('/admin')


@blueprint.route('/admin/logout')
def logout() -> Any:
    """
    Logout action route.
    """
    auth_service.do_logout()
    return redirect('/admin')

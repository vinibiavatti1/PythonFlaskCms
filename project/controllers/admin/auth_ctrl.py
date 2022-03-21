"""
Admin auth endpoints.
"""
from typing import Any
from werkzeug.utils import redirect
from flask import Blueprint, request, render_template, flash
from project.validators import auth_validator
from project.services import auth_service


# Blueprint
blueprint = Blueprint(
    'admin_auth_ctrl',
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
        auth_service.process_login(login_data)
        context = login_data['context']
        return redirect(f'/{context}/admin/articles')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect('/admin')


@blueprint.route('/admin/logout')
def logout() -> str:
    """
    Logout action route.
    """
    auth_service.do_logout()
    return render_template('/public/login.html')

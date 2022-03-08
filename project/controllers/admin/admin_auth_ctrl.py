from werkzeug.utils import redirect
from project.errors import ValidationError
from flask import Blueprint, request, render_template, flash
from markupsafe import escape
from project.validators import auth_validator
from project.services import auth_service
from project.config import config


# Blueprint
blueprint = Blueprint('admin_auth', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/admin', methods=['GET'])
def login():
    return render_template('/admin/login.html')


@blueprint.route('/admin', methods=['POST'])
def login_action():
    # Validate data and ReCaptcha
    try:
        auth_validator.validate_login_data(request.form)
        if config['recaptcha_enabled']:
            auth_validator.validate_recaptcha(
                request.form.get('recaptcha-token')
            )
    except ValidationError as err:
        flash(err, category='danger')
        return render_template('/public/login.html')

    # Do login
    email = escape(request.form.get('email'))
    password = request.form.get('password')
    if auth_service.do_login(email, password):
        return redirect('/')
    flash('Invalid user and/or password', category='danger')
    return render_template('/public/login.html')


@blueprint.route('/admin/logout')
def logout():
    auth_service.do_logout()
    return render_template('/public/login.html')

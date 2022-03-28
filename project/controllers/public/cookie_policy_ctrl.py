from flask import Blueprint, request, make_response, redirect
from project.enums import cookie_enum


# Blueprint
blueprint = Blueprint(
    'admin_cookie_policy_ctrl',
    __name__,
    url_prefix='/cookie-policy'
)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/agree')
def agree():
    response = make_response(redirect(request.referrer))
    response.set_cookie(cookie_enum.COOKIE_POLICY, '1')
    return response


@blueprint.route('/disagree')
def disagree():
    response = make_response(redirect(request.referrer))
    response.set_cookie(cookie_enum.COOKIE_POLICY, '0')
    return response

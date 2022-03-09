"""
Authentication service module.
"""
from typing import Any
from flask import session
from project.enums import session_enum
from project.enums import permission_enum
from project.repositories import user_repository
from project.services import property_service
from project.utils import security_utils
from markupsafe import escape
from project.errors import AuthError
import requests


###############################################################################
# Private Functions
###############################################################################


def __validate_recaptcha(token: str) -> None:
    """
    Validate Google reCaptcha.

    Validate the score of the ReCaptcha token. ReCaptcha v3 returns a score
    (1.0 is very likely a good interaction, 0.0 is very likely a bot).
    """
    recaptcha_secret_key = property_service.get_property(
        'recaptcha_secret_key'
    )
    recaptcha_threshold = property_service.get_property(
        'recaptcha_threshold'
    )
    response = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': recaptcha_secret_key,
            'response': token,
        }
    )
    message = 'Invalid ReCaptcha. Please, try again.'
    if response.status_code != 200:
        raise AuthError(message)
    json = response.json()
    if not json['success']:
        raise AuthError(message)
    if json['score'] <= recaptcha_threshold:
        raise AuthError(message)


###############################################################################
# Public Functions
###############################################################################


def do_login(email: str, password: str) -> None:
    """
    Authenticate user to application.
    """
    password_sha256 = security_utils.generate_hash(password)
    users = user_repository.select_by_email_and_password(
        email,
        password_sha256
    )
    if len(users) != 1:
        raise AuthError('Invalid user and/or password')
    user = users[0]
    session[session_enum.USER_ID] = user['id']
    session[session_enum.USER_NAME] = user['name']
    session[session_enum.USER_EMAIL] = user['email']
    session[session_enum.USER_PERMISSION] = user['permission']


def do_logout() -> None:
    """
    Destroy user session.
    """
    session.clear()


def process_login(login_data: dict[str, Any]) -> None:
    """
    Process login authentication.
    """
    recaptcha_enabled = property_service.get_property('recaptcha_enabled')
    if recaptcha_enabled == '1':
        __validate_recaptcha(str(login_data.get('recaptcha-token')))
    email = escape(login_data.get('email'))
    password = str(login_data.get('password'))
    do_login(email, password)

"""
Authentication service module.
"""
from typing import Any
from flask import session
from project.enums import session_enum
from project.repositories import user_repository
from project.services import property_service
from project.utils import security_utils
from markupsafe import escape
from project.errors import AuthError
from project.enums import string_types_enum
import requests


def validate_recaptcha(context: str, token: str) -> None:
    """
    Validate Google reCaptcha.

    Validate the score of the ReCaptcha token. ReCaptcha v3 returns a score
    (1.0 is very likely a good interaction, 0.0 is very likely a bot).
    """
    recaptcha_secret_key = property_service.get_property_value(
        context,
        'recaptcha_secret_key'
    )
    recaptcha_threshold = property_service.get_property_value(
        context,
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


def do_login(email: str, password: str) -> dict[str, Any]:
    """
    Authenticate user to application.
    """
    password_sha256 = security_utils.generate_hash(password)
    user = user_repository.select_by_email_and_password(
        email,
        password_sha256
    )
    if user is None:
        raise AuthError('Invalid user and/or password')
    return user


def do_logout() -> None:
    """
    Destroy user session.
    """
    session.clear()


def initialize_session(context: str, user: dict[str, Any]) -> None:
    """
    Set session data.
    """
    session[session_enum.CONTEXT] = context
    session[session_enum.USER_ID] = user['id']
    session[session_enum.USER_EMAIL] = user['email']
    session[session_enum.USER_NAME] = user['name']
    session[session_enum.USER_PERMISSION] = user['permission']


def process_login(context: str, login_data: dict[str, Any]) -> None:
    """
    Process login authentication.
    """
    recaptcha_enabled = \
        property_service.get_property_value(context, 'recaptcha_enabled')
    if recaptcha_enabled == string_types_enum.TRUE:
        validate_recaptcha(context, str(login_data.get('recaptcha-token')))
    user = do_login(escape(login_data['email']), login_data['password'])
    initialize_session(login_data['context'], user)
    user_repository.update_last_login(user['id'])

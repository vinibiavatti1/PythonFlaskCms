from flask import session
from project.enums import session_enum
from project.enums import permission_enum
from project.repositories import user_repository


def do_login(email: str, password: str) -> bool:
    """
    Authenticate user to application
    """
    users = user_repository.select_by_email_and_password(email, password)
    if len(users) != 1:
        return False
    user = users[0]
    session[session_enum.USER_ID] = user['id']
    session[session_enum.USER_NAME] = user['name']
    session[session_enum.USER_EMAIL] = user['email']
    session[session_enum.USER_PERMISSION] = user['permission']
    return True


def do_logout() -> None:
    """
    Destroy user session
    """
    session.clear()

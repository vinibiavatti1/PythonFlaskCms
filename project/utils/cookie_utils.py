"""
Cookie utilities.
"""
from typing import Optional
from flask import request
from project.enums import cookie_enum


def cookie_policy_consent() -> Optional[bool]:
    """
    Return the user cookie consent.

    Return True if user accepted the cookie policy, False if not, or None if
    the user didn't answer anything.
    """
    answer = request.cookies.get(cookie_enum.COOKIE_POLICY, None)
    if answer is not None:
        return True if answer == '1' else False
    else:
        return None


def get_idiom(default: Optional[str] = None) -> str:
    """
    Return the idiom in the session.
    """
    return request.cookies.get(cookie_enum.IDIOM, default)

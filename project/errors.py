"""
App exceptions.
"""


class AppError(Exception):
    """
    Base application error.
    """


class ValidationError(AppError):
    """
    Application validation error.
    """


class TranslationError(AppError):
    """
    Translation errors.
    """


class AuthError(AppError):
    """
    Authentication errors.
    """


class EntityError(AppError):
    """
    Entity errors.
    """

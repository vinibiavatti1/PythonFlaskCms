"""
User model.
"""
from project.utils import security_utils


class BuiltinUserModel:
    """
    User model.
    """

    def __init__(self, *, name: str, email: str, password: str,
                 permission: str) -> None:
        """
        Create an user model.
        """
        self.password = security_utils.generate_hash(password)
        self.name = name
        self.email = email
        self.password = password
        self.permission = permission

"""
Default admin users.
"""
from project.models.user_model import UserModel
from project.enums import permission_enum


users: list[UserModel] = [
    UserModel(
        name='Admin',
        email='admin@admin.com',
        password='admin',
        permission=permission_enum.ADMINISTRATOR
    )
    # Add more...
]

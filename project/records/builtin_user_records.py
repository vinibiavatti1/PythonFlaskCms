"""
Default admin users.
"""
from project.models.builtin_user_model import BuiltinUserModel
from project.enums import permission_enum


builtin_user_records: list[BuiltinUserModel] = [
    BuiltinUserModel(
        name='Admin',
        email='admin@admin.com',
        password='admin',
        permission=permission_enum.ADMINISTRATOR
    )
    # Add more...
]

"""
Custom URLs records module.
"""
from project.models.custom_url_model import CustomUrlModel


custom_urls: list[CustomUrlModel] = [
    CustomUrlModel(
        url='/member/logout',
        description='Action to logout the member.',
    ),
    CustomUrlModel(
        url='/locale/<locale>',
        description='Action to set the idiom in cookie',
    ),
    # Add more...
]

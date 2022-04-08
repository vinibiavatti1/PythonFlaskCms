"""
Default translations.
"""
from project.models.translation_model import TranslationModel
from project.enums import string_types_enum as str_type


translation_records: list[TranslationModel] = [
    TranslationModel(
        name='cookie_policy_title',
        value='Cookie Policy',
        active=str_type.TRUE,
    ),
    TranslationModel(
        name='cookie_policy_content',
        value='We use cookies to improve user experience, and analyze website '
              'traffic. For these reasons, we may share your site usage data '
              'with our analytics partners. By clicking "Agree" you consent '
              'to store on your device all the technologies used in the '
              'application',
        active=str_type.TRUE,
    ),
    TranslationModel(
        name='cookie_policy_agree',
        value='Agree',
        active=str_type.TRUE,
    ),
    TranslationModel(
        name='cookie_policy_disagree',
        value='Disagree',
        active=str_type.TRUE,
    ),
    TranslationModel(
        name='cookie_policy_cancel',
        value='Cancel',
        active=str_type.TRUE,
    ),
    TranslationModel(
        name='error_not_found',
        value='The page was not found',
        active=str_type.TRUE,
    ),
    TranslationModel(
        name='error_unauthorized',
        value='You must authenticate to access this resource',
        active=str_type.TRUE,
    ),
    TranslationModel(
        name='error_bad_request',
        value='Error to process the request. Please, try again.',
        active=str_type.TRUE,
    ),
    TranslationModel(
        name='error_forbidden',
        value='You don\'t have access rights to access this content',
        active=str_type.TRUE,
    ),
    TranslationModel(
        name='error_internal_server',
        value='An internal server error occurred. Please, try again. If the '
              'same error continues, contact the administrator.',
        active=str_type.TRUE,
    ),
    # Add more...
]

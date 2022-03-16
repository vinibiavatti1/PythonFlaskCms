"""
Default translations.
"""
from project.models.translation_model import TranslationModel


translations: list[TranslationModel] = [
    TranslationModel(
        idiom='en',
        name='cookie_policy_title',
        value='Cookie Policy',
    ),
    TranslationModel(
        idiom='en',
        name='cookie_policy_content',
        value='We use cookies to improve user experience, and analyze website '
              'traffic. For these reasons, we may share your site usage data '
              'with our analytics partners. By clicking "Agree" you consent '
              'to store on your device all the technologies used in the '
              'application',
    ),
    TranslationModel(
        idiom='en',
        name='cookie_policy_agree',
        value='Agree',
    ),
    TranslationModel(
        idiom='en',
        name='cookie_policy_disagree',
        value='Disagree',
    ),
    TranslationModel(
        idiom='en',
        name='cookie_policy_cancel',
        value='Cancel',
    ),
    TranslationModel(
        idiom='en',
        name='error_not_found',
        value='The page was not found',
    ),
    TranslationModel(
        idiom='en',
        name='error_unauthorized',
        value='You must authenticate to access this resource',
    ),
    TranslationModel(
        idiom='en',
        name='error_bad_request',
        value='Error to process the request. Please, try again.',
    ),
    TranslationModel(
        idiom='en',
        name='error_forbidden',
        value='You don\'t have access rights to access this content',
    ),
    TranslationModel(
        idiom='en',
        name='error_internal_server',
        value='An internal server error occurred. Please, try again. If the '
              'same error continues, contact the administrator.',
    ),
    # Add more...
]

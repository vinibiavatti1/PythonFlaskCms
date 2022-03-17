"""
Informations records module.
"""
from typing import Union
from project.models.information_model import InformationModel
from project.models.header_model import HeaderModel


informations: list[Union[InformationModel, HeaderModel]] = [

    ###########################################################################
    # Action URLs
    ###########################################################################

    HeaderModel(
        'Action URLs'
    ),
    # TODO
    InformationModel(
        name='Login URL',
        description='Para with authentication form for members.',
        value='/page/<idiom>/login',
    ),
    InformationModel(
        name='Blog URL',
        description='Blog page that will render the published posts.',
        value='/page/<idiom>/blog',
    ),
    InformationModel(
        name='FAQ URL',
        description='Page that will render all FAQs records.',
        value='/page/<idiom>/faq',
    )

    ###########################################################################
    # Action URLs
    ###########################################################################

    # Add more...
]

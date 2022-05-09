"""
Component records.
"""
from project.models.object_model import ObjectModel
from project.enums import object_enum
from project.properties.components.footer_properties \
    import footer_properties
from project.properties.components.navbar_properties \
    import navbar_properties


component_records: list[ObjectModel] = [
    ObjectModel(
        name=object_enum.NAVBAR_COMPONENT,
        description='Navbar component',
        icon='bi-window',
        is_content=False,
        properties=navbar_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),
    ObjectModel(
        name=object_enum.FOOTER_COMPONENT,
        description='Footer component',
        icon='bi-window-desktop',
        is_content=False,
        properties=footer_properties,
        allow_actions=True,
        template=None,
        children=[],
    ),
]

"""
Content records.
"""
from project.models.object_model import ObjectModel
from project.enums import object_enum
from project.properties.contents.article_properties \
    import article_properties
from project.properties.contents.custom_properties \
    import custom_properties
from project.properties.contents.event_properties \
    import event_properties
from project.properties.contents.landing_properties \
    import landing_properties
from project.properties.contents.news_properties \
    import news_properties
from project.properties.contents.post_properties \
    import post_properties


content_records: list[ObjectModel] = [
    ObjectModel(
        name=object_enum.ARTICLE_CONTENT,
        description='Article content',
        icon='bi-files',
        is_content=True,
        properties=article_properties,
        allow_actions=True,
        template='article.html',
        children=[
            object_enum.HEADER_BLOCK
        ],
    ),
    ObjectModel(
        name=object_enum.EVENT_CONTENT,
        description='Event content',
        icon='bi-calendar-event',
        is_content=True,
        properties=event_properties,
        allow_actions=True,
        template='event.html',
        children=[
            object_enum.HEADER_BLOCK
        ],
    ),
    ObjectModel(
        name=object_enum.NEWS_CONTENT,
        description='News content',
        icon='bi-newspaper',
        is_content=True,
        properties=news_properties,
        allow_actions=True,
        template='news.html',
        children=[
            object_enum.HEADER_BLOCK
        ],
    ),
    ObjectModel(
        name=object_enum.POST_CONTENT,
        description='Post content',
        icon='bi-pin-angle',
        is_content=True,
        properties=post_properties,
        allow_actions=True,
        template='post.html',
        children=[
            object_enum.HEADER_BLOCK
        ],
    ),
    ObjectModel(
        name=object_enum.CUSTOM_CONTENT,
        description='Custom content',
        icon='bi-filetype-html',
        is_content=True,
        properties=custom_properties,
        allow_actions=True,
        template='custom.html',
        children=[],
    ),
]

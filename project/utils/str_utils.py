"""
String utility functions.
"""


def title(text: str, *, plural: bool = False) -> str:
    """
    Transform string to title removing "_" chars.
    """
    text = text.replace('_', ' ')
    if plural:
        text += 's'
    return text.title()

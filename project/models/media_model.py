"""
Media model.
"""


class MediaModel:
    """
    Model of media.
    """

    def __init__(self, *, name: str, path: str, extension: str,
                 file_type: str) -> None:
        """
        Init media object.
        """
        self.name = name
        self.path = path
        self.extension = extension
        self.file_type = file_type

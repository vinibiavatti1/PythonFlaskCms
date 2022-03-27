"""
File model.
"""


class FileModel:
    """
    Model of file.
    """

    def __init__(self, *, name: str, path: str, extension: str,
                 file_type: str) -> None:
        """
        Init file object.
        """
        self.name = name
        self.path = path
        self.extension = extension
        self.file_type = file_type

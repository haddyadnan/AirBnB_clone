#!/usr/bin/python3


"""
This modules contains pseudo function
to test invoking of FileStorage methods with no return
"""

from models.engine.file_storage import *
from models.engine.file_storage import FileStorage


class FileStorage(FileStorage):

    """
    tmp FileStorage
    """

    def __init__(self) -> None:
        super().__init__()

    def new(self):
        """
        return True if Success
        """
        return True

    def reload(self):
        """
        return True if Success
        """
        return True

    def save(self):
        """
        return True if Success
        """
        return True

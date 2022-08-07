#!/usr/bin/python3

"""
This module contains test cases for filestorage module
"""

from models.engine.file_storage import FileStorage
import unittest


class TestFStorageInit(unittest.TestCase):

    """
    Test File Storage Init
    """

    def test_init(self):
        model = FileStorage()
        self.assertIsInstance(model, FileStorage)

    def test_args(self):
        model = FileStorage()
        model.name = "home"
        model.save()
        self.assertFalse(hasattr(model, "home"))

    def test_docs(self):
        self.assertIsNotNone(FileStorage.__doc__)

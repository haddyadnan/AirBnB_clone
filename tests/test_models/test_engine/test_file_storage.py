#!/usr/bin/python3

"""
This module contains test cases for filestorage module
"""

from models.engine.file_storage import FileStorage
from models.engine.tmp_file_storage import FileStorage as F
from models.base_model import BaseModel
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

    def test__file_path(self):
        with self.assertRaises(AttributeError):
            FileStorage().__file_path

    def test__objects(self):
        with self.assertRaises(AttributeError):
            FileStorage().__objects

    def test_all(self):
        fs = FileStorage().all()
        self.assertIsInstance(fs, dict)

    def test_new(self):
        fs = F().new()
        self.assertTrue(fs)

    def test_reload(self):
        fs = F().reload()
        self.assertTrue(fs)

    def test_save(self):
        fs = F().save()
        self.assertTrue(fs)

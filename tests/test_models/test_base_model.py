#!/usr/bin/python3

"""
Unittest for base model
"""
from curses import has_key
from genericpath import exists
import unittest

from models.base_model import BaseModel
from datetime import datetime


class TestBaseInit(unittest.TestCase):

    """
    Test BaseModel Init
    """

    def test_init(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_time(self):
        model = BaseModel()
        self.assertEqual(model.created_at, model.updated_at)

    def test_kwinit1(self):
        model = BaseModel()
        model.first_name = "test"
        self.assertEqual(model.first_name, "test")

    def test_ca_dt_type(self):
        model = BaseModel()
        self.assertEqual(type(model.created_at), datetime)

    def test_ua_dt_type1(self):
        model = BaseModel()
        self.assertEqual(type(model.updated_at), datetime)

    def test_docs(self):
        self.assertIsNotNone(BaseModel.__doc__)


class TestBaseSave(unittest.TestCase):
    """
    Test class Method - Save
    """

    def test_save_file(self):
        model = BaseModel()
        model.name = "test"
        model.save()
        self.assertEqual(True, exists("file.json"))

    def test_update_time(self):
        model = BaseModel()
        model.name = "test"
        prev = model.updated_at
        model.save()
        update = model.updated_at
        self.assertGreater(update, prev)

    def test_docs(self):
        self.assertIsNotNone(BaseModel.save.__doc__)


class TestBaseTDict(unittest.TestCase):
    """
    Test class Method - to_dict
    """

    def test_to_dict_dtype(self):
        model = BaseModel()
        self.assertEqual(type(model.to_dict()), dict)

    def test_to_dict_content(self):
        model = BaseModel()
        dct = model.to_dict()
        self.assertTrue("id" in dct.keys())
        self.assertTrue("created_at" in dct.keys())
        self.assertTrue("updated_at" in dct.keys())
        self.assertTrue("__class__" in dct.keys())

    def test_to_dict_content_change(self):
        model = BaseModel()
        model.first_name = "hello"
        dct = model.to_dict()
        self.assertTrue("id" in dct.keys())
        self.assertTrue("created_at" in dct.keys())
        self.assertTrue("updated_at" in dct.keys())
        self.assertTrue("__class__" in dct.keys())
        self.assertTrue("first_name" in dct.keys())

    def test_docs(self):
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

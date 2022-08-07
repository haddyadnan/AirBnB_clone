#!/usr/bin/python3

"""
This module contains test cases for user module
"""

from models.user import User
from models.base_model import BaseModel
import unittest


class TestBaseInit(unittest.TestCase):

    """
    Test BaseModel Init
    """

    def test_init(self):
        model = User()
        self.assertIsInstance(model, User)

    def test_inheritance(self):
        model = User()
        self.assertIsInstance(model, BaseModel)

    def test_args(self):
        model = User()
        model.name = "home"
        model.save()
        self.assertFalse(hasattr(model, "home"))

    def test_docs(self):
        self.assertIsNotNone(User.__doc__)

    # def test_time(self):
    #     model = User()
    #     self.assertEqual(model.created_at, model.updated_at)

    # def test_kwinit1(self):
    #     model = User()
    #     model.first_name = "test"
    #     self.assertEqual(model.first_name, "test")

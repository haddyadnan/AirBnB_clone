#!/usr/bin/python3

"""
This module contains test cases for user module
"""

from models.user import User
from models.base_model import BaseModel
import unittest


class TestBaseInit(unittest.TestCase):

    """
    Test User Init
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

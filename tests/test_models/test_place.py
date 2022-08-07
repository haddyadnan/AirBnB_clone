#!/usr/bin/python3

"""
This module contains test cases for place module
"""

from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlaceInit(unittest.TestCase):

    """
    Test BaseModel Init
    """

    def test_init(self):
        model = Place()
        self.assertIsInstance(model, Place)

    def test_inheritance(self):
        model = Place()
        self.assertIsInstance(model, BaseModel)

    def test_args(self):
        model = Place()
        model.name = "home"
        model.save()
        self.assertFalse(hasattr(model, "home"))

    def test_docs(self):
        self.assertIsNotNone(Place.__doc__)

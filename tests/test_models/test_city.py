#!/usr/bin/python3

"""
This module contains test cases for city module
"""

from models.city import City
from models.base_model import BaseModel
import unittest


class TestUserInit(unittest.TestCase):

    """
    Test BaseModel Init
    """

    def test_init(self):
        model = City()
        self.assertIsInstance(model, City)

    def test_inheritance(self):
        model = City()
        self.assertIsInstance(model, BaseModel)

    def test_args(self):
        model = City()
        model.name = "home"
        model.save()
        self.assertFalse(hasattr(model, "home"))

    def test_docs(self):
        self.assertIsNotNone(City.__doc__)

    # def test_time(self):
    #     model = City()
    #     self.assertEqual(model.created_at, model.updated_at)

    # def test_kwinit1(self):
    #     model = City()
    #     model.first_name = "test"
    #     self.assertEqual(model.first_name, "test")

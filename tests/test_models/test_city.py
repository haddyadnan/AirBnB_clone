#!/usr/bin/python3

"""
This module contains test cases for city module
"""

from models.city import City
from models.base_model import BaseModel
import unittest


class TestUserInit(unittest.TestCase):

    """
    Test City Init
    """

    def test_init(self):
        model = City()
        model.save()
        self.assertIsInstance(model, City)

    def test_inheritance(self):
        model = City()
        self.assertIsInstance(model, BaseModel)

    def test_args(self):
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_docs(self):
        self.assertIsNotNone(City.__doc__)

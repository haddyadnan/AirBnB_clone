#!/usr/bin/python3

"""
This module contains test cases for user module
"""

from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenityInit(unittest.TestCase):

    """
    Test Amenity Init
    """

    def test_init(self):
        model = Amenity()
        self.assertIsInstance(model, Amenity)

    def test_inheritance(self):
        model = Amenity()
        self.assertIsInstance(model, BaseModel)

    def test_args(self):
        model = Amenity()
        model.name = "home"
        model.save()
        self.assertFalse(hasattr(model, "home"))

    def test_docs(self):
        self.assertIsNotNone(Amenity.__doc__)

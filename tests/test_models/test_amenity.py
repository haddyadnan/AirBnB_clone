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
        model.save()
        self.assertIsInstance(model, Amenity)

    def test_inheritance(self):
        model = Amenity()
        self.assertIsInstance(model, BaseModel)

    def test_args(self):
        self.assertEqual(Amenity.name, "")

    def test_docs(self):
        self.assertIsNotNone(Amenity.__doc__)

#!/usr/bin/python3

"""
This module contains test cases for place module
"""

from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlaceInit(unittest.TestCase):

    """
    Test place Init
    """

    def test_init(self):
        model = Place()
        model.save()
        self.assertIsInstance(model, Place)

    def test_inheritance(self):
        model = Place()
        self.assertIsInstance(model, BaseModel)

    def test_args(self):
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

    def test_docs(self):
        self.assertIsNotNone(Place.__doc__)

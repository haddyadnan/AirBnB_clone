#!/usr/bin/python3

"""
This module contains test cases for Review module
"""

from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReviewInit(unittest.TestCase):

    """
    Test Review Init
    """

    def test_init(self):
        model = Review()
        self.assertIsInstance(model, Review)

    def test_inheritance(self):
        model = Review()
        self.assertIsInstance(model, BaseModel)

    def test_args(self):
        model = Review()
        model.name = "home"
        model.save()
        self.assertFalse(hasattr(model, "home"))

    def test_docs(self):
        self.assertIsNotNone(Review.__doc__)

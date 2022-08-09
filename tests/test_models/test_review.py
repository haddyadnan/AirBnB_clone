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

    def test_review_attr(self):
        model = Review()
        model.place_id = "id"
        model.user_id = "user"
        model.text = "text"

        self.assertEqual("id", model.place_id)
        self.assertEqual("user", model.user_id)
        self.assertEqual("text", model.text)

    def test_docs(self):
        self.assertIsNotNone(Review.__doc__)

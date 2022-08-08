#!/usr/bin/python3

"""
This module contains test cases for state module
"""

from models.state import State
from models.base_model import BaseModel
import unittest


class TestStateInit(unittest.TestCase):

    """
    Test State Init
    """

    def test_init(self):
        model = State()
        model.save()
        self.assertIsInstance(model, State)

    def test_inheritance(self):
        model = State()
        self.assertIsInstance(model, BaseModel)

    def test_args(self):
        model = State()
        model.name = "home"
        model.save()
        self.assertFalse(hasattr(model, "home"))

    def test_docs(self):
        self.assertIsNotNone(State.__doc__)

    def test_state_name(self):
        model = State()
        model.name = "test"
        self.assertEqual("test", model.name)

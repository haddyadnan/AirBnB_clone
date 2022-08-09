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

    def test_args(self):
        self.assertEqual(State.name, "")

    def test_docs(self):
        self.assertIsNotNone(State.__doc__)


if __name__ == "__main__":
    unittest.main()

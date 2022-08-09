#!/usr/bin/python3

"""
This module contains test cases for user module
"""

from models.user import User
from models.base_model import BaseModel
import unittest


class TestUserInit(unittest.TestCase):

    """
    Test User Init
    """

    def test_init(self):
        model = User()
        self.assertIsInstance(model, User)

    def test_inheritance(self):
        model = User()
        self.assertIsInstance(model, BaseModel)

    def test_args(self):
        model = User()
        model.name = "home"
        model.save()
        self.assertFalse(hasattr(model, "home"))

    def test_docs(self):
        self.assertIsNotNone(User.__doc__)


class TestUserAttr(unittest.TestCase):
    """
    Test User attributes
    """

    def test_User_email(self):
        user = User()
        user.email = "test"
        user.save()
        self.assertEqual("test", user.email)

    def test_User_password(self):
        user = User()
        user.password = "root"
        self.assertEqual("root", user.password)

    def test_User_first_name(self):
        user = User()
        user.first_name = "test"
        self.assertEqual("test", user.first_name)

    def test_User_last_name(self):
        user = User()
        user.last_name = "test"
        self.assertEqual("test", user.last_name)


if __name__ == '__main__':
    unittest.main()

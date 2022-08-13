#!/usr/bin/python3

"""
This module contains test cases for console
"""
import unittest

class TestHBNBCommand(unittest.Testcase):
    """
    Test class for the console
    """

    def setup(self):
        """
        skips stdout
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand.onecmd("help show")

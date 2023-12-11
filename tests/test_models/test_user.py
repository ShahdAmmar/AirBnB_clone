#!/usr/bin/python3
"""Module for test User class that tests basemodel"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test User class implementation"""

    def test_inheritance(self):
        """ Test that User inherits from BaseModel """
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """ Test types of class attributes """
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_documentation(self):
        """class documentation"""
        self.assertGreater(len(User.__doc__), 1)


if __name__ == '__main__':
    unittest.main()

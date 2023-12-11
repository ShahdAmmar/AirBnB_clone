#!/usr/bin/python3
""" Review class test """
import unittest
from models.review import Review
from models.base_model import BaseModel


class Review_test(unittest.TestCase):
    """class to test class State and its attributes"""
    def test_inheritance(self):
        """Method to checks if test_user inherits from Base_model"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Method to test the attribute name in class state"""
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

    def documentation_test(self):
        """ class documentation """
        self.assertGreater(len(Review.__doc__), 1)


if __name__ == "__main__":
    unittest.main()

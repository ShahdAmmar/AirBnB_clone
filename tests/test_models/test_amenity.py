#!/usr/bin/python3
""" Amenity class test """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class Amenity_test(unittest.TestCase):
    """class to test class State and its attributes"""
    def test_inheritance(self):
        """Method to checks if test_user inherits from Base_model"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """Method to test the attribute name in class state"""
        self.assertIsInstance(Amenity.name, str)

    def documentation_test(self):
        """ class documentation """
        self.assertGreater(len(Amenity.__doc__), 1)
    '''
    def initdocumentation_test(self):
        """ class documentation """
        self.assertGreater(len(Amenity.__init__.__doc__), 1)
    '''
    


if __name__ == "__main__":
    unittest.main()

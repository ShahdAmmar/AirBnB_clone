#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class City_test(unittest.TestCase):
    """class to test class State and its attributes"""
    def test_inheritance(self):
        """Method to checks if test_user inherits from Base_model"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Method to test the attribute name in class state"""
        self.assertIsInstance(City.name, str)
        self.assertIsInstance(City.state_id, str)

    def documentation_test(self):
        """ class documentation """
        self.assertGreater(len(City.__doc__), 1)

    '''
    def initdocumentation_test(self):
        """ class documentation """
        self.assertGreater(len(City.__init__.__doc__), 1)
    '''


if __name__ == "__main__":
    unittest.main()

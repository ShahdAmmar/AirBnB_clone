#!/usr/bin/python3
""" State class test """
import unittest
from models.state import State
from models.base_model import BaseModel


class State_test(unittest.TestCase):
    """class to test class State and its attributes"""
    def test_inheritance(self):
        """Method to checks if test_user inherits from Base_model"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Method to test the attribute name in class state"""
        self.assertIsInstance(State.name, str)

    def documentation_test(self):
        """ class documentation """
        doct = State.__doc__
        self.assertGreater(len(doct), 1)
    '''
    def initdocumentation_test(self):
        """ class documentation """
        self.assertGreater(len(State.__init__.__doc__), 1)
    '''


if __name__ == "__main__":
    unittest.main()

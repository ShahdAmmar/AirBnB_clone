#!/usr/bin/python3
""" Place class test """
import unittest
from models.place import Place
from models.base_model import BaseModel


class Place_test(unittest.TestCase):
    """class to test class State and its attributes"""
    def test_inheritance(self):
        """Method to checks if test_user inherits from Base_model"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """Method to test the attribute name in class state"""
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)

    def documentation_test(self):
        """ class documentation """
        self.assertGreater(len(Place.__doc__), 1)

    '''
    def initdocumentation_test(self):
        """ class documentation """
        self.assertGreater(len(Place.__init__.__doc__), 1)

    '''


if __name__ == "__main__":
    unittest.main()

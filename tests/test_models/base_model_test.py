#!/usr/bin/python3
"""
test for the base_model class
"""
import unittest
from models.base_model import BaseModel

class TestBasemodel(unittest.TestCase):
    """class to test the BaseModel class"""
    def test_init(self):
        """Method to test the id, created_at, and updated-at"""
        model_class = BaseModel()

        self.assertIsNotNone(model_class.id)
        self.assertIsNotNone(model_class.created_at)
        self.assertIsNotNone(model_class.updated_at)

    def test_save(self):
        """Method to test the save class"""
        model_class = BaseModel()
        inital = model_class.updated_at
        current = model_class.save()

        self.assertNotEqual(inital, current)

    def test_to_dict(self):
        """Method to test to_dict class"""
        model_class = BaseModel()
        dict_base_model = model_class.to_dict()

        self.assertIsInstance(dict_base_model, dict)

        self.assertEqual(dict_base_model["__class__"], 'BaseModel')
        self.assertEqual(dict_base_model["id"], model_class.id)
        self.assertEqual(dict_base_model["created_at"], model_class.created_at.isoformat())
        self.assertEqual(dict_base_model["updated_at"], model_class.updated_at.isoformat())

    def test_str(self):
        """Method to test __str__ class"""
        model_class = BaseModel()

        self.assertTrue(str(model_class).startswith('[BaseModel]')) #returns true when it starts with BaseModel
        self.assertIn(model_class.id, str(model_class)) #test that the id of the instance created is at string representation
        self.assertIn(str(model_class.__dict__), str(model_class)) #tests that the instance has additional string representation


if __name__ == "__main__":
    unittest.main()

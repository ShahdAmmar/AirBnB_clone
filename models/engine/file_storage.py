#!/usr/bin/python3
""" Module of FileStorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """serilizes instances to JSON and deserialized JSON file to instances

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.

    """
    __file_path = 'file3.json'
    __objects = {}

    def all(self):
        """ returns __objects dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj:
            key = f'{obj.__class__.__name__}.{obj.id}'
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to JSON file """
        nw_dict = {}
        for key, val in FileStorage.__objects.items():
            nw_dict[key] = val.to_dict().copy()
        with open(FileStorage.__file_path, 'w') as jsonFile:
            json.dump(nw_dict, jsonFile)

    def reload(self):
        """ deserializes JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as jsonFile:
                nw_dict = json.load(jsonFile)
            for key, val in nw_dict.items():
                cls_name = val.get('__class__')
                # print(cls_name)
                obj = eval(cls_name + '(**val)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass

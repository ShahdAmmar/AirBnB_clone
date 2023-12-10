#!/usr/bin/python3
"""A base module for all models in the project"""

import uuid
from datetime import datetime
import models


class BaseModel:

    """A base model for all models"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at
        when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Method that returns all the values
        and keys of __dict__ of instance"""
        ins_dic = dict(self.__dict__)
        ins_dic["__class__"] = self.__class__.__name__
        ins_dic["created_at"] = self.created_at.isoformat()
        ins_dic["updated_at"] = self.updated_at.isoformat()

        return ins_dic

    def __str__(self):
        """Returns the string representation of an instance"""
        cls_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls_name, self.id, self.__dict__)

#!/usr/bin/python3
""" A class City that inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class """
    state_id = ""
    name = ""
    """
    def __init__(self, *args, **kwargs):
        ''' intialize inherited attributes '''
        super.__init__(*args, **kwargs)
    """

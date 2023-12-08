#!/usr/bin/python3
""" A class Review that inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class """
    place_id = ""
    user_id = ""
    text = ""
    '''
    def __init__(self, *args, **kwargs):
        """ intialize inherited attributes """
        super.__init__(*args, **kwargs)
    '''

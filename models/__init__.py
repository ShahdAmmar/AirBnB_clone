#!/usr/bin/python3
""" create a unique FileStorage instance for your application """
from models.engine.file_storage import FileStorage

""" creating instance of FileStorage, called storage """
storage = FileStorage()
storage.reload()

#!/usr/bin/python3

"""This module instantiates an object of class FileStorage"""

from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


var = getenv('HBNB_TYPE_STORAGE')
if var == 'db':
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
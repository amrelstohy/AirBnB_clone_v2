#!/usr/bin/python3

"""This module instantiates an object of class FileStorage"""

from os import getenv

var = getenv('HBNB_TYPE_STORAGE')
if var == 'db':
    from models.engine.db_storage import DBStorage
    from models.state import State
    storage = DBStorage()
    storage.reload()
    print(storage.all())
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
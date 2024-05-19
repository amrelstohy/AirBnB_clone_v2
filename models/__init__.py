#!/usr/bin/python3

"""This module instantiates an object of class FileStorage"""

import os

storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == 'db':
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()
storage.reload()

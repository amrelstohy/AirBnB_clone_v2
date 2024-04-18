#!/usr/bin/python3
"""
db store engine
"""

from sqlalchemy import create_engine
from models.base_model import Base
import os
from sqlalchemy.orm import sessionmaker,scoped_session


class DBStorage():
    """
    db storgae system
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        init function
        """
        user = os.getenv('HBNB_MYSQL_USER')
        db = os.getenv('HBNB_MYSQL_DB')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        test = os.getenv('HBNB_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format
                                        (user, passwd, host, db), pool_pre_ping=True)
        if test == 'tets':
            Base.metadata.drop_all(bind=self.__engine)



    def all(self, cls=None):
        """
        getting all objects of the db tables
        """
        data = {}
        from models import user, city, amenity, place, review, state
        classes = [user.User, state.State, city.City, amenity.Amenity, place.Place, review.Review]
        if cls is None:
            all_classes = classes
        else:
            all_classes = [cls]
        for clss in all_classes:
            objects = self.__session.query(state.State).all()
            for obj in objects:
                data[f"{clss.__name__}.{obj.id}"] = obj
        return data
            
    def new(self, obj):
        """
        new object addition
        """
        self.__session.add(obj)
    
    def save(self):
        """
        commits the changes
        """
        self.__session.commit()

    def reload(self):
        """
        Reload the db tables
        """
        Base.metadata.create_all(self.__engine)


    def delete(self, obj=None):
        """
        deleting db session
        """
        if obj:
            self.__session.delete(obj)
            self.save()
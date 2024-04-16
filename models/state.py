#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import Relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = Relationship("City", cascade="all, delete-orphan", backref='state')
    @property
    def cities(self):
        from models import storage
        from models.city import City
        return [attr for attr in storage.all(City).values() if City.state_id == self.id]

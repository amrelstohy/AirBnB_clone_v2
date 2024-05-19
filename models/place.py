#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Table, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(), default=0, nullable=False)
    number_bathrooms = Column(Integer(), default=0, nullable=False)
    max_guest = Column(Integer(), default=0, nullable=False)
    price_by_night = Column(Integer(), default=0, nullable=False)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    amenity_ids = []
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        users = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place")
        place_amenity = Table("place_amenity",
            Base.metadata,
            Column("place_id",
                String(60),
                ForeignKey("places.id"),
                primary_key=True,
                nullable=False),
            Column("amenity_id",
                String(60),
                ForeignKey("amenities.id"),
                primary_key=True,
                nullable=False)
            )
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    else:
        @property
        def reviews(self):
            from models import storage
            from models.review import Review
            data = []
            for obj in storage.all(Review).values():
                if obj.place_id == self.id:
                    data.append(obj)
            return data
        
        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            data = []
            for obj in storage.all(Amenity).values():
                if obj.id in self.amenity_ids:
                    data.append(obj)
            return data
        
        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel,\
    Base, Column, String, Integer, ForeignKey, Float, relationship
from os import getenv
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

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
    # amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        relationship('Review', cascade='all, delete', backref='place')
    else:
        @property
        def reviews(self):
            from models import storage
            all_reviews = storage.all(Review)
            review = []
            for obj in all_reviews.values():
                if obj.place_id == self.place.id:
                    review.append(obj)
            return review

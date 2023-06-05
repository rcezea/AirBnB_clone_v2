#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'


if getenv("HBNB_TYPE_STORAGE") == "db":
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
else:
    name = ''

    @property
    def cities(self):
        """
        Returns the join of city and state
        """
        from models import storage
        all_cities = storage.all(City)
        city = []
        city_obj = all_cities.values()
        for obj in city_obj:
            if obj.state_id == self.id:
                city.append(obj)
        return city

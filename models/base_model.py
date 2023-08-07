#!/usr/bin/python3


"""BaseModel"""

import datetime
import uuid
import models


class BaseModel:
    """
    Class that defines all common methods/attributes
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """Arguments for the constructor dof a BaseModel"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for keys, value in kwargs.items():
                if keys == "__class__":
                    continue
                if keys == 'id':
                    self.id = value
                elif keys == 'created_at':
                    self.created_at = datetime.datetime.fromisoformat(value)
                elif keys == 'updated_at':
                    self.updated_at = datetime.datetime.fromisoformat(value)
                else:
                    setattr(self, keys, value)

    def __str__(self):
        """Print"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__})"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        return dict(self.__dict__, **{'__class__':
                    self.__class__.__name__, 'created_at':
                    self.created_at.isoformat(), 'updated_at':
                    self.updated_at.isoformat()})

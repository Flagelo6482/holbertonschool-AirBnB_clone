#!/usr/bin/python3


"""BaseModel"""

import datetime as dt
import uuid
import models

class BaseModel:
    """
    Class that defines all common methods/attributes
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialization constructor"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k == 'id':
                    self.id = v
                elif k == 'created_at':
                    self.created_at = dt.datetime.fromisoformat(v)
                elif k == 'updated_at':
                    self.updated_at = dt.datetime.fromisoformat(v)
                else:
                    setattr(self, k, v)

    def __str__(self):
        """Returns a user-readable string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at public instance
        attribute with the current date and time
        """
        self.updated_at = dt.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary with the set values
        """
        return dict(self.__dict__, **{'__class__':
                    self.__class__.__name__, 'created_at':
                    self.created_at.isoformat(), 'updated_at':
                    self.updated_at.isoformat()})

#!/usr/bin/python3


"""BaseModel"""

import datetime as dt
import uuid


class BaseModel:
    """
    Class that defines all common methods/attributes
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialization constructor"""
        if kwargs:
            if '__clas__' in kwargs:
                del kwargs['__class__']
                for k, v in kwargs.items():
                    date = '%Y-%m-%dT%H:%M:%S.%f'
                    if k in ['created_at', 'updated_at']:
                        v = dt.datetime.strptime(v, date)
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a user-readable string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at public instance
        attribute with the current date and time
        """
        self.updated_at = dt.datetime.now()

    def to_dict(self):
        """
        Return a dictionary with the set values
        """
        dic = self.__dict__
        dic['__class__'] = type(self).__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        dic['id'] = self.id
        return dic

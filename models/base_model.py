#!/usr/bin/python3


"""BaseModel"""

import models
import datetime as dt
import uuid


class BaseModel:
    """
    Class that defines all common methods/attributes
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialization constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = dt.datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            class_name = kwargs.pop('__class__', None)
            if class_name:
                date = "%Y-%m-%dT%H:%M:%S.%f"
                for key, value in kwargs.items():
                    if key in ['created_at', 'updated_at']:
                        value = dt.datetime.strptime(value, date)
                    setattr(self, key, value)
        if not kwargs:
            models.storage.new(self)

    def __str__(self):
        """Returns a user-readable string"""
        st_dic = vars(self)
        return f"[{self.__class__.__name__}] ({self.id}) {st_dic}"

    def save(self):
        """
        Updates the updated_at public instance
        attribute with the current date and time
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary with the set values
        """
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        dic['id'] = self.id
        return dic

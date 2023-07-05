#!/usr/bin/python3


"""BaseModel"""

import datetime
import uuid


class BaseModel:
    """
    Class that defines all common methods/attributes
    for other classes
    """
    def __init__(self):
        """Initialization constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

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

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
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """
        Updates the updated_at public instance
        attribute with the current date and time
        """
        self.updated_at = datetime.datetime.now()

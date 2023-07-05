#!/usr/bin/python3


"""BaseModel"""

import datetime
import uuid


class BaseModel:
    """
    Class that defines all common methods/attributes
    for other classes
    """
    id = str()
    created_at = 0
    updated_at = 0

    def __init__(self):
        """Initialization constructor"""
        id = str(uuid.uuid4())
        created_at = datetime.now()

    def __str__(self):
        """Print a string readable to a user"""
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """Update the date and time"""
        updated_at = datetime.now()

    def to_dict(self):
        """Returns the dictionary of the object"""
        return f"{self.__dict__}"

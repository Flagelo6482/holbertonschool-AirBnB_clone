#!/usr/bin/python3


"""This class inherits from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """This class has one attribute"""
    place_id = ""
    user_id = ""
    text = ""

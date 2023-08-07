#!/usr/bin/python3


"""This class inherits from BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """This class has one attribute"""
    state_id = ""
    name = ""

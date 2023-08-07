#!/usr/bin/python3


"""Class User that inherits from BaseModel"""


from models.base_model import BaseModel


class User(BaseModel):
    """This class has public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

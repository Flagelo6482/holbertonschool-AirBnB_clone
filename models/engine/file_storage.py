#!/usr/bin/python3
"""This class serializes instances to a JSON file
and deserializes JSON file to instances"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class has attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        d1 = {}
        with open(self.__file_path, "w") as f:
            for key, value in self.__objects.items():
                d1[key] = value.to_dict()
            f.write(json.dumps(d1))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        cls = ["BaseModel", "User", "State", "City",
               "Place", "State", "Amenity", "Review"]
        try:
            with open(self.__file_path, 'r') as f:
                diccionario = json.loads(f.read())
            for key in diccionario.keys():
                value = diccionario[key]
                if value['__class__'] in cls:
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass

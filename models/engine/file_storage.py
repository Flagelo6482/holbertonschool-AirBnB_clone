#!/usr/bin/python3


"""Store first object"""


import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the diccionario __objectcs"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dic = {}
        with open(self.__file_path, mode="w") as file:
            for k, v in self.__objects.items():
                dic[k] = v.to_dict()
            file.write(json.dumps(dic))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode="r") as file:
                dic = json.loads(file.read())
            self.__objects = dic
        except FileNotFoundError:
            pass

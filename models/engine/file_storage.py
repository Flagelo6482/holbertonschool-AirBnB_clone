#!/usr/bin/python3


"""Store first object"""


import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}{self.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, mode="w") as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        des_j = {}
        if self.__file_path:
            with open(self.__file_path, mode="r") as file:
                des_son = json.loads(file)
                des_j.append(des_son)

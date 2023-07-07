#!/usr/bin/python3


"""Store first object"""


import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{self.id}"
        self.__objects[key] = obj

    def save(self):
        serialized = {}
        for k, obj in self.__objects.items():
            serialized[k] = obj.to_dict()

        with open(self.__file_path, mode="w") as file:
            json.dump(serialized, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split(".")
                    module = __import__("models." + class_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

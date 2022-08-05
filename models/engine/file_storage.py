#!/usr/bin/python3

"""
This module contains the class for persistent file storage
"""

from genericpath import exists
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City


class FileStorage:

    """
    class file storage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):

        """
        returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):

        """
        Args:
            obj -
        sets in __objects the obj with key <obj class name>.id
        """
        obj_key = obj.__class__.__name__ + "." + obj.id

        FileStorage.__objects[obj_key] = obj
        ##############DEBUGGING#############
        # print()
        # print("This is the object")
        # print(obj)
        # print(obj, "------------------object")
        # print(obj.__dict__, "----------------dict")

    def save(self) -> None:

        """
        serialiazes objects to __file_path
        """
        json_obj = {}
        for key, value in FileStorage.__objects.items():
            # print(f"The value is: {value}")
            json_obj[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_obj, f)

    def reload(self) -> None:

        """
        deserializes the json file to __objects if __file_path exists
        """

        if exists(FileStorage.__file_path):
            FileStorage.__objects = {}
            with open(FileStorage.__file_path, "r") as f:
                load_dict = json.load(f)
                # print()
                # print()
                # print("------- RELOADING HERE ----------")
                # print(load_dict.items())
                # print("-------------------DONE--------------")
                # print()
                for k, v in load_dict.items():
                    cls_name = k.split(".")[0]
                    FileStorage.__objects[k] = eval(cls_name)(**v)
                # print(FileStorage.__objects)
                # print("________FINALLY DONE_____________")

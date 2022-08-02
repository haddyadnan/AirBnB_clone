#!/usr/bin/python3

"""
This module contains the class for persistent file storage
"""

from cgi import FieldStorage
from genericpath import exists
import json


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

    def save(self) -> None:

        """
        serialiazes objects to __file_path
        """
        json_obj = {}
        for key, value in FileStorage.__objects.items():
            json_obj[key] = str(value)
        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_obj, f)

    def reload(self) -> None:

        """
        deserializes the json file to __objects if __file_path exists
        """
        # obj = {}
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                load_dict = json.load(f)
            # storage = json.loads(FileStorage.__file_path)
            for k, v in load_dict.items():
                FileStorage.__objects[k] = v

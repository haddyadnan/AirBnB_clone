#!/usr/bin/python3

"""
This module contains the Base Model for the AirBnB Clone - Console Project
"""


import uuid
from datetime import datetime
import models


class BaseModel:

    """class Base Model"""

    def __init__(self, *args, **kwargs) -> None:

        """
        Initialize Base model with kwargs if any passed
                else initialize BaseModel with new input
        """

        if any(args):
            pass

        if kwargs:
            fmt = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, fmt)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)  # models.storage to avoid circular import

    def save(self) -> None:

        """
        Public instance method: save
        updates the attribute updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:

        """
        Public instance method: to_dict
        returns dict containing all keys/values of __dict__ of the instance
        """

        tmp_dict = self.__dict__.copy()
        for k, v in tmp_dict.items():
            if k in ["created_at", "updated_at"]:
                tmp_dict[k] = v.isoformat()

        tmp_dict["__class__"] = self.__class__.__name__

        return tmp_dict

    def __str__(self) -> str:

        """
        String format
        """

        str_fmt = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return str_fmt

    def attr_update(self, attr_dict=None):
        """
        Updates a BaseModel object
        """

        do_not_update = ['id', 'created_at', 'updated_at']
        if attr_dict:
            to_update = {k: v for k, v in attr_dict.items()
                         if k not in do_not_update}
            for k, v in to_update.items():
                setattr(self, k, v)
            self.save()

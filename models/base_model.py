#!/usr/bin/python3

"""
This module contains the Base Model for the AirBnB Clone - Console Project
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """class Base Model"""

    def __init__(self, *args, **kwargs) -> None:

        """
        Initialize Base model with kwargs if any passed
                else initialize BaseModel with new input
        """

        if any(args):
            pass

        if any(kwargs):
            fmt = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], fmt)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], fmt)
            for key, value in kwargs.items():
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self) -> None:

        """
        Public instance method: save
        updates the attribute updated_at with the current datetime
        """

        self.created_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:

        """
        Public instance method: to_dict
        returns dict containing all keys/values of __dict__ of the instance
        """

        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()

        return self.__dict__

    def __str__(self) -> str:

        """
        String format
        """

        str_fmt = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return str_fmt

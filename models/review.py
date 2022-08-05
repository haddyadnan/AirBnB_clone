#!/usr/bin/python3

"""
This module contains the Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):

    """
    Implementation of the Review class
    Attr:
        place_id
        user_id
        text
    """

    place_id = ""
    user_id = ""
    text = ""

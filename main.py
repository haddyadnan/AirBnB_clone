#!/usr/bin/python3

from models.base_model import BaseModel
from datetime import datetime

my_model = BaseModel()
# print("_________Before___________")
# print(my_model)
# prev = my_model.updated_at
# my_model.nigger = "nigger"
# print("_________After___________")
# my_model.save()
# print(my_model.updated_at > prev)
# # d = datetime(my_model.updated_at)
# # print(d)
a = my_model.to_dict()
print(a.keys(), type(a.keys()))

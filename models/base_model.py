#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    def __str__(self) -> str:
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    def save(self):
        self.updated_at = datetime.utcnow()
        return self.updated_at
    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        value = my_model_json[key]
        print("\t{}: ({}) - {}".format(key, type(value), value))

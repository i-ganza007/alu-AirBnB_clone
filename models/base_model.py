import uuid
import datetime
class BaseModel:
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self) -> str:
        return f'[{BaseModel.__name__}] ({self.id}) {self.__dict__}'
        
    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()
        return self.updated_at

# In the method below , We used the copy() method for the __dict__ so that we can avoid affecting the actual attributes .
    def to_dict(self):
        MyDict = self.__dict__.copy()
        MyDict['__class__'] = BaseModel.__name__
        return MyDict

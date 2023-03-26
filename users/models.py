from typing import Optional
from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel


class Gender(str, Enum):
  female = "female"
  male = "male"

class User(BaseModel):
  user_id: UUID = uuid4()
  name: str
  email: str
  age: int
  gender: Gender
  
class UserEdit(BaseModel):
  name: Optional[str]
  email: Optional[str]
  age: Optional[int]
  gender: Optional[Gender]
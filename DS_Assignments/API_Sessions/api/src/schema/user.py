from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

class UserIn(BaseModel):
    email: str
    password: str

class UserDB(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    email: str
    password: str
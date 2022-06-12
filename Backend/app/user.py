from email import message
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    userName: str
    password: str
    
    def toJson(self):
        data = {"firstName" : self.firstName, "lastName" : self.lastName, "email": self.email, "userName": self.userName, "password" : self.password}
        return data

from email import message
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    userName: str
    password: str

    def changePassword(self, oldPass: str, newPass: str):
        if oldPass == self.password:
            self.password = newPass
            return True
        else:
            return False
    
    def forgotPassword(self, userName: str, newPass: str):
        if userName == self.userName:
            self.password = newPass



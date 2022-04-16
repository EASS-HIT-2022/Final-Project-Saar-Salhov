from ast import And, If
from collections import UserList
from email import message
from typing import List
from fastapi import FastAPI
import time
from matplotlib.pyplot import flag
from pydantic import BaseModel
from product import Product
from Receipts import Receipts
from user import User


app = FastAPI()
usersList = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/getUsers")
async def getUsers():
    return {"message": usersList}

@app.post("/register")
async def register(bUser: User):
    flag = False
    for user in usersList:
        if user.userName == bUser.userName:
            message =  {"message": "The username " +  user.userName + " is already exist"}
            flag = True
    if flag == False:
        usersList.append(bUser)
        message = {f"message": "The user " + bUser.firstName + " " + bUser.lastName + " was created successfuly"}
    return message

@app.post("/changePassword")
async def changePassword(bUsername: str,bOldPass: str, bNewPass: str):
    flag = False
    isPassChanged = False

    for user in usersList:
        if user.userName == bUsername:
            flag = True
            isPassChanged = user.changePassword(bOldPass, bNewPass)
            break
    if isPassChanged == True:
        return {"message": "Password Changed"}
    elif flag == False:
        return {"message": "The username you entered is not exist"}
    else:
        return {"message": "The old password is incorrect"}

@app.post("/sighnIn")
async def sighnIn(bUsername: str, bPassword: str):
    flag = False

    for user in usersList:
        if user.userName == bUsername and user.password == bPassword:
            flag = True
            message = {"message":"You have successfully logged in"}
            return message
    if flag == False:
        message = {"message":"Username or password is incorrect"}
    return message



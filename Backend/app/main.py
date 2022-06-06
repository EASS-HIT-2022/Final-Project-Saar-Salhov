from ast import And, If
from collections import UserList
from email import message
from typing import List
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
import time
from matplotlib.pyplot import flag
from pydantic import BaseModel, EmailStr
import uvicorn
from product import Product
from Receipts import Receipts
from user import User



app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8001",
    "http://frontend:3000",
    "http://frontend:8001",
    "http://frontend:8000",
    "http://frontend:8080",
    "http://Frontend:3000",
    "http://Frontend:8001",
    "http://Frontend:8000",
    "http://Frontend:8080",
    "*"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

usersList = []
listOfReceipts = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/getUsers")
async def getUsers():
    return {"message": usersList}

@app.post("/register")
async def register(bUser: User):
    for user in usersList:
        if user.userName == bUser.userName:
            raise HTTPException(status_code=404, detail="The username " +  user.userName + " is already exist")
    usersList.append(bUser)
    message = {f"message": "The user " + bUser.firstName + " " + bUser.lastName + " was created successfuly"}
    return message

@app.put("/changePassword")
async def changePassword(bUsername: str = Body(),bOldPass: str = Body(), bNewPass: str = Body()):
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
        raise HTTPException(status_code=400, detail="The username you entered is not exist")
    else:
        raise HTTPException(status_code=400, detail="The old password is incorrect")

@app.post("/signIn")
async def sighnIn(bUsername: str = Body(), bPassword: str = Body()):
    flag = False

    for user in usersList:
        if user.userName == bUsername and user.password == bPassword:
            flag = True
            message = {"message":"You have successfully logged in"}
    if flag == False:
        raise HTTPException(status_code=400, detail="Username or password is incorrect")
    return message

@app.get("/getAllmyReceipts")
async def getAllReceipts(username: str):
    receiptForSpecificUser = []
    for receipt in listOfReceipts:
        if username == receipt.username:
            receiptForSpecificUser.append(receipt)
    return {"message": receiptForSpecificUser}

@app.get("/getAllReceipts")
async def getAllReceipts():
    return {"message": listOfReceipts}

@app.post("/uploadReceipt")
async def uploadReceipt(bReceipt: Receipts):
    listOfReceipts.append(bReceipt)
    return {"message": "The recieipt uploaded successfully"}




from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from numpy import true_divide
from Receipts import Receipts
from user import User
import mysqlConnector
import json
import mongoDbConnector
 

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8001",
    "http://localhost:7000",
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
    con = mysqlConnector.connect()
    selectAllUsers = ("SELECT * FROM users")

    cursor = con.cursor()
    cursor.execute(selectAllUsers)
    myresult = cursor.fetchall()
    cursor.close()
    con.close()

    return {"message": myresult}

@app.post("/register")
async def register(bUser: User):
    con = mysqlConnector.connect()
    selectAllUsers = ("SELECT userName FROM users")
    addUser = ("INSERT INTO users "
              "(firstName, lastName, email, userName, password) "
              "VALUES (%(firstName)s, %(lastName)s, %(email)s, %(userName)s,%(password)s)")
    
    cursor = con.cursor()
    cursor.execute(selectAllUsers)

    for (userName, ) in cursor:
        if userName == bUser.userName:
            raise HTTPException(status_code=404, detail="The username " +  userName + " is already exist")


    cursor.execute(addUser, bUser.toJson())
    con.commit()
    cursor.close()
    con.close()
    message = {f"message": "The user " + bUser.firstName + " " + bUser.lastName + " was created successfuly"}
    
    return message

@app.put("/changePassword")
async def changePassword(bUsername: str = Body(default="string"),bOldPass: str = Body(default="string"), bNewPass: str = Body(default="string")):
    isPassChanged = False
    con = mysqlConnector.connect()
    selectAllUsers = ("SELECT userName, password FROM users WHERE userName=%s")
    updateNewPassword = "UPDATE users SET password = %s WHERE userName = %s"

    cursor = con.cursor()
    cursor.execute(selectAllUsers,(bUsername,))

    for (userName, password) in cursor:
        if userName == bUsername and password == bOldPass:
            isPassChanged = True
            val = (bNewPass, userName)
            cursor.execute(updateNewPassword, val)
            con.commit()
            break

    cursor.close()
    con.close()

    if isPassChanged == True:
        return {"message": "Password Changed"}
    else:
        raise HTTPException(status_code=400, detail="The username or the old password you entered is not exist")

@app.post("/signIn")
async def sighnIn(bUsername: str = Body(default="string"), bPassword: str = Body(default="string")):
    con = mysqlConnector.connect()
    selectAllUsers = ("SELECT userName, password FROM users WHERE userName=%s and password=%s")
    val = (bUsername, bPassword)
    isUserExist = False

    cursor = con.cursor()
    cursor.execute(selectAllUsers,val)
    
    for (userName, password) in cursor:
        if userName == bUsername and password == bPassword:
            isUserExist = True

    if isUserExist:
        message = {"message":"You have successfully logged in"}
    else:
        raise HTTPException(status_code=400, detail="Username or password is incorrect")
    return message

@app.get("/getAllmyReceipts")
async def getAllReceipts(username: str):
    con = mongoDbConnector.connect()
    receiptForSpecificUser = []

    for receipt in con.find({"username": username},{'_id':0}):
        receiptForSpecificUser.append(receipt)

    return {"message": receiptForSpecificUser}

@app.get("/getAllReceipts")
async def getAllReceipts():
    listOfReceipts = []
    con = mongoDbConnector.connect()

    for receipt in con.find({},{'_id':0}):
        listOfReceipts.append(receipt)

    return {"message": listOfReceipts}

@app.post("/uploadReceipt")
async def uploadReceipt(bReceipt: Receipts):
    con = mongoDbConnector.connect()
    con.insert_one(json.loads(bReceipt.json())).inserted_id
    return {"message": "The recieipt uploaded successfully"}




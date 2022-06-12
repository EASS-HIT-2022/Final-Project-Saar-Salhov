from wsgiref import headers
from fastapi.testclient import TestClient
from httplib2 import Credentials
from pytest import TestReport
from main import app

import json


client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}

def test_get_users():
    response = client.get("getUsers/")
    assert response.status_code == 200
    assert response.json() == {'message': []}


def test_register_first_user():
    response = client.post("/register", json={
  "firstName": "saar",
  "lastName": "salhov",
  "email": "saar@example.com",
  "userName": "saarsalhov",
  "password": "Aa123456"
})
    assert response.status_code == 200
    assert response.json() == {f"message": "The user saar salhov was created successfuly"}

def test_register_with_existing_username():
    response = client.post("/register", json={
  "firstName": "saar",
  "lastName": "salhov",
  "email": "saar@example.com",
  "userName": "saarsalhov",
  "password": "Aa123456"
})
    assert response.status_code == 404
    assert response.json() == {"detail": "The username saarsalhov is already exist"}

def test_change_password():
    response = client.put("/changePassword",json={ 
    "bUsername": "saarsalhov",
    "bOldPass": "Aa123456",
    "bNewPass": "Bb123456"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Password Changed"}

def test_change_password_bad_username():
    response = client.put("/changePassword", json={
"bUsername": "saar",
"bOldPass": "Aa123456",
"bNewPass": "Bb123456"
})
    assert response.status_code == 400
    assert response.json() == {"detail": "The username or the old password you entered is not exist"}


def test_sign_in():
    response = client.post("/signIn", json={
"bUsername": "saarsalhov",
"bPassword": "Bb123456",
})
    assert response.status_code == 200
    assert response.json() == {"message": "You have successfully logged in"}

def test_sign_in_with_bad_credentials():
    response = client.post("/signIn", json={
"bUsername": "saarsalhov",
"bPassword": "Bb1236",
})
    assert response.status_code == 400
    assert response.json() == {"detail": "Username or password is incorrect"}

def test_get_receipts():
    response = client.get("getAllReceipts/")
    assert response.status_code == 200
    assert response.json() == {'message': []}

def test_add_receipts():
    response = client.post("/uploadReceipt", json={
    "date": "2022-06-12",
    "username": "saar",
    "storeName": "Renuar",
    "products": [
    {
        "name": "T-shirt",
        "color": "Red",
        "price": 100
        },
    {
        "name": "pants",
        "color": "Green",
        "price": 50
        },
    {
        "name": "hat",
        "color": "Blue",
        "price": 20
        }
    ]
})
    assert response.status_code == 200
    assert response.json() == {"message": "The recieipt uploaded successfully"}

def test_get_all_my_receipts():
    response = client.get("getAllmyReceipts/?username=saar")
    assert response.status_code == 200
    assert response.json() == {'message': [{
    "date": "2022-06-12",
    "username": "saar",
    "storeName": "Renuar",
    "products": [
    {
        "name": "T-shirt",
        "color": "Red",
        "price": 100
        },
    {
        "name": "pants",
        "color": "Green",
        "price": 50
        },
    {
        "name": "hat",
        "color": "Blue",
        "price": 20
        }
    ]
}]}
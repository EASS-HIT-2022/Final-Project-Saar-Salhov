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
    response = client.post("/changePassword",params={ 
    "bUsername": "saarsalhov",
    "bOldPass": "Aa123456",
    "bNewPass": "Bb123456"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Password Changed"}

def test_change_password_bad_username():
    response = client.post("/changePassword", params={
"bUsername": "saar",
"bOldPass": "Aa123456",
"bNewPass": "Bb123456"
})
    assert response.status_code == 400
    assert response.json() == {"detail": "The username you entered is not exist"}

def test_change_password_bad_old_pass():
    response = client.post("/changePassword", params={
"bUsername": "saarsalhov",
"bOldPass": "Aa1234",
"bNewPass": "Bb123456"
})
    assert response.status_code == 400
    assert response.json() == {"detail": "The old password is incorrect"}

def test_sign_in():
    response = client.post("/signIn", params={
"bUsername": "saarsalhov",
"bPassword": "Bb123456",
})
    assert response.status_code == 200
    assert response.json() == {"message": "You have successfully logged in"}

def test_sign_in_with_bad_credentials():
    response = client.post("/signIn", params={
"bUsername": "saarsalhov",
"bPassword": "Bb1236",
})
    assert response.status_code == 400
    assert response.json() == {"detail": "Username or password is incorrect"}






"""
Defines the blueprint for the User
"""
from flask import Blueprint, request
import json

from models import User
from .utils import (
    check_password,
    generate_password_hash,
    is_email_exists,
    is_password_correct,
    generate_jwt
)

USER_BLUEPRINT = Blueprint("user", __name__)

@USER_BLUEPRINT.route('/register', methods=["POST"])
def createUser():
    data = json.loads(request.data)
    if not check_password(data):
        return {"error": "Passwords do not match"}, 400
    if "email" not in data:
        return {"error": "Email is mandatory"}, 400
    if (is_email_exists(data["email"])):
        return {"error": "Email already exists"}, 409
    key, salt = generate_password_hash(data["password"])
    user = User(
        name = data["name"],
        email = data["email"],
        passwordHash = key,
        passwordSalt = salt,
        phoneNumber = data["phoneNumber"],
        isAdmin = False)
    user.save()
    return {'data': "User Registered Successfuly!"}, 201


@USER_BLUEPRINT.route('/login', methods=["POST"])
def loginUser():
    data = json.loads(request.data)
    for user in User.objects(email=data["email"]):
        if not is_password_correct(data["password"], user.passwordSalt, user.passwordHash):
            return {"error": "Wrong Password..."}, 401
        # generate JWT
        token, exp_time = generate_jwt(user)
        return {"access_token" : 'Bearer ' + token, "expiresOn" : exp_time}, 200
    
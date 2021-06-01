import hashlib
import os
import datetime
import jwt
from models import User


def check_password(data={}):
    return (
        "password" in data
        and "confirmPassword" in data
        and data["password"] == data["confirmPassword"]
    )


def generate_password_hash(password):
    salt = os.urandom(32).hex()
    key = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000
    ).hex()
    return key, salt


def is_email_exists(email):
    return User.objects(email=email)


def is_password_correct(password, passwordSalt, passwordHash):
    salt = bytes.fromhex(passwordSalt).hex()
    key = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000
    ).hex()
    return key == passwordHash


def generate_jwt(user):
    exp_time = datetime.datetime.now() + datetime.timedelta(hours=24)
    payload = {"user": user.email, "exp": exp_time}
    token = jwt.encode(payload, "SECRET_KEY")
    return token, exp_time

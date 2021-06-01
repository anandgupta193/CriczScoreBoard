from mongoengine import StringField, IntField, EmailField, DateTimeField, BooleanField
import mongoengine_goodjson as GoodJSON
import datetime


class User(GoodJSON.Document):
    name = StringField(required=True)
    passwordHash = StringField(max_length=100, required=True)
    passwordSalt = StringField(max_length=100, required=True)
    email = EmailField(max_length=50, required=True, unique=True)
    phoneNumber = IntField()
    createdAt = DateTimeField(default=datetime.datetime.now())
    isAdmin = BooleanField(required=True)

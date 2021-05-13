from mongoengine import StringField, IntField, EmailField, DateTimeField, BooleanField
import mongoengine_goodjson as GoodJSON

class User(GoodJSON.Document):
   name = StringField(required=True)
   passwordHash = StringField(max_length=50, required=True)
   email = EmailField(max_length=50, required=True)
   phoneNumber = IntField()
   createdAt = DateTimeField(required=True)
   isAdmin = BooleanField(required=True)
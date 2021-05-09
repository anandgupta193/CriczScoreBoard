from mongoengine import *
import mongoengine_goodjson as gj

class Player(gj.Document):
   playerId = StringField(required=True)
   name = StringField(max_length=50)
   age = IntField()
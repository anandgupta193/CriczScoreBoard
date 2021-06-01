from mongoengine import StringField, IntField
import mongoengine_goodjson as GoodJSON


class Player(GoodJSON.Document):
    playerId = StringField(required=True)
    name = StringField(max_length=50)
    age = IntField()

from mongoengine import StringField
import mongoengine_goodjson as GoodJSON

class Team(GoodJSON.Document):
   teamid = StringField(required=True)
   teamname = StringField(max_length=50)
   
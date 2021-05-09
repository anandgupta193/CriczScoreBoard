from mongoengine import *
import mongoengine_goodjson as gj

class Team(gj.Document):
   teamid = StringField(required=True)
   teamname = StringField(max_length=50)
   
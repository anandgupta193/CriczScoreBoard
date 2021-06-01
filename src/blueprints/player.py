"""
Defines the blueprint for the Player
"""
from flask import Blueprint, request
from models import Player
import json
import logging
from decorators import authorize


PLAYER_BLUEPRINT = Blueprint("player", __name__)


@PLAYER_BLUEPRINT.route("/players", methods=["GET"])
@authorize
def getPlayers():
    logging.info("GetPlayers Entry")
    players = Player.objects
    logging.info("GetPlayers Exit")
    return {"data": json.loads(players.to_json())}


@PLAYER_BLUEPRINT.route("/player", methods=["POST"])
def createPlayer():
    data = json.loads(request.data)
    createdRecord = Player(
        age=data["age"], playerId=data["playerId"], name=data["name"]
    ).save()
    return {"data": json.loads(createdRecord.to_json())}, 201


@PLAYER_BLUEPRINT.route("/player", methods=["PATCH"])
def updatePlayer():
    args = dict(request.args)
    player = Player.objects(playerId=args["playerId"])
    player.update(name=json.loads(request.data)["name"])
    return {"data": json.loads(player.to_json())}


@PLAYER_BLUEPRINT.route("/player", methods=["DELETE"])
def deletePlayer():
    args = dict(request.args)
    player = Player.objects(playerId=args["playerId"])
    player.delete()
    return {"data": json.loads(player.to_json())}

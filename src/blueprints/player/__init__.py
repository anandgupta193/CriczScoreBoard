"""
Defines the blueprint for the players
"""

from flask import Blueprint

PLAYER_BLUEPRINT = Blueprint("player", __name__)

@PLAYER_BLUEPRINT.route('/players')
def getPlayers():
    return {'message': 'Hello from CricketScroz, You have access to out Players'}
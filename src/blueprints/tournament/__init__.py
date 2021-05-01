"""
Defines the blueprint for the Tournaments
"""

from flask import Blueprint

TOURNAMENT_BLUEPRINT = Blueprint("tournament", __name__)

@TOURNAMENT_BLUEPRINT.route('/tournaments')
def getTournament():
    return {'message': 'Hello from CricketScroz, You have access to out Tournaments'}
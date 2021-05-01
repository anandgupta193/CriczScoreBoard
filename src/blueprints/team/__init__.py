"""
Defines the blueprint for the Teams
"""

from flask import Blueprint

TEAM_BLUEPRINT = Blueprint("team", __name__)

@TEAM_BLUEPRINT.route('/teams')
def getTeam():
    return {'message': 'Hello from CricketScroz, You have access to out Teams'}
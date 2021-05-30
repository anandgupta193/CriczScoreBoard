"""
Defines the blueprint for the Tournaments
"""

from flask import Blueprint

TOURNAMENT_BLUEPRINT = Blueprint("tournament", __name__)


@TOURNAMENT_BLUEPRINT.route('/tournaments')
def getTournament():
    return {
        'message': 'You have access to out Tournaments'
        }

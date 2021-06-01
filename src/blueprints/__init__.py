import logging

"""
List of all blueprints
"""

from blueprints.player import PLAYER_BLUEPRINT
from blueprints.team import TEAM_BLUEPRINT
from blueprints.user import USER_BLUEPRINT


init = "Blueprints Initialized with"
logging.debug(f"{init}, {PLAYER_BLUEPRINT}, {TEAM_BLUEPRINT}, {USER_BLUEPRINT}")

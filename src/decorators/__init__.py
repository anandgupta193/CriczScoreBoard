import logging

"""
List of all blueprints
"""

from decorators.loginRequired import authorize

init = "Blueprints Initialized with"
logging.debug(f"login required decorators, {authorize}")

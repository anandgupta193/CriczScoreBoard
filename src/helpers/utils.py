from flask import Blueprint
import blueprints
import config

def registerBlueprints(server):
    for blueprint in vars(blueprints).values():
        if isinstance(blueprint, Blueprint):
            server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

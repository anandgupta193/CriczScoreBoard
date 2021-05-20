from flask import Blueprint, Flask, abort, jsonify
import blueprints
import config
from werkzeug.exceptions import HTTPException

def registerBlueprints(server):
    for blueprint in vars(blueprints).values():
        if isinstance(blueprint, Blueprint):
            server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)


def registerErrorHandler(server):
    @server.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(error=str(e)), code
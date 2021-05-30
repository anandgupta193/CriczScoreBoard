from flask import Blueprint, jsonify
import blueprints
import config
from werkzeug.exceptions import HTTPException
import logging
from flask_swagger_ui import get_swaggerui_blueprint


def registerBlueprints(server):
    for blueprint in vars(blueprints).values():
        if isinstance(blueprint, Blueprint):
            server.register_blueprint(
                blueprint, url_prefix=config.APPLICATION_ROOT
                )


def registerErrorHandler(server):
    @server.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(error=str(e)), code


def registerLogger():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.INFO)
    logging.basicConfig(**config.LOG_CONFIG)


def registerSwagger(server):
    configuration = {
        'app_name': config.APP_NAME
        }
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config=configuration
    )
    server.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

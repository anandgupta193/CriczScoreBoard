from flask import Blueprint
from werkzeug.utils import send_from_directory

SWAGGER_BLUEPRINT = Blueprint("swagger", __name__)


@SWAGGER_BLUEPRINT.route('/static/swagger.json')
def send_static(path):
    return send_from_directory('static', 'swagger.json')

from flask import Flask
from flask import Blueprint

import config
import blueprints

server = Flask(__name__)

server.debug = config.DEBUG

for blueprint in vars(blueprints).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

server.run(host=config.HOST, port=config.PORT)
from flask import Flask
from flask import Blueprint
from mongoengine import connect

import config
import blueprints

server = Flask(__name__)
connect(config.DB_NAME, host='localhost', port=27017, username='root', password='rootpassword', authentication_source='admin')


for blueprint in vars(blueprints).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

server.run(host=config.HOST, port=config.PORT)
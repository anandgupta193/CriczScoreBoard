from flask import Flask
from mongoengine import connect

import config
import helpers.utils as Utils

server = Flask(__name__)

"""
DB Connection
"""
connect(
    config.DB_NAME,
    host=config.DB_HOST,
    port=config.DB_PORT,
    username=config.DB_USER,
    password=config.DB_PASS,
    authentication_source=config.DB_AUTH_SOURCE
    )

"""
Registering Blueprints
"""
Utils.registerBlueprints(server)

"""
Registering Error Handler
"""
Utils.registerErrorHandler(server)

server.run(host=config.HOST, port=config.PORT)
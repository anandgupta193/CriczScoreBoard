from flask import Flask
from mongoengine import connect
import config
import helpers.utils as Utils


server = Flask(__name__)

server.debug = config.DEBUG

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

"""
Registering Logger
"""
Utils.registerLogger()

"""
Registering Swagger
"""

Utils.registerSwagger(server)

server.run(host=config.HOST, port=config.PORT)

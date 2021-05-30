import os
import logging


APPLICATION_ROOT = '/api'
DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
HOST = HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))
SECRET_KEY = os.getenv("SECRET_KEY")

DB_NAME = "cricScorz"
APP_NAME = "cricScorz"
DB_HOST = "localhost"
DB_PORT = 27017
DB_USER = "root"
DB_PASS = "rootpassword"
DB_AUTH_SOURCE = "admin"

LOG_CONFIG = {
    'filename': 'reports/appLogs/server.log',
    'filemode': 'a',
    'format': '%(asctime)s, %(msecs)d %(name)s %(levelname)s %(message)s',
    'datefmt': '%H:%M:%S',
    'level': logging.INFO
    }

import os

APPLICATION_ROOT='/api'
DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
HOST=HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))

DB_CONTAINER = os.getenv("APPLICATION_DB_CONTAINER", "db")
DB_URI = ""
DB_NAME = "cricScorz"
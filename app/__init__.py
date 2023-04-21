"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13ab8rddl13a55tk10-a.oregon-postgres.render.com",
        database="todo_viwr",
        user="todo_viwr_user",
        password="4YT2cX1IvYN5SsFyVh4oOzsO2fFSt4fl")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

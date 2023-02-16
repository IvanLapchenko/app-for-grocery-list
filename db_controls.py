from random import random

from flask import g
import sqlite3
from grocery_list import app
import random


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('app.db')
        cursor = db.cursor()
        cursor.execute("select name from groceries")
        all_data = cursor.fetchall()
        all_data = [str(val[0]) for val in all_data]

        shopping_list = all_data.copy()
        random.shuffle(shopping_list)
        shopping_list = shopping_list[:5]
        return all_data, shopping_list


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


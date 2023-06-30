from views import db
from _config import DATABASE_PATH

import sqlite3
from datetime import datetime
from views import app


with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()
    #with app.app_context():
        #db.c*reate_all()
    
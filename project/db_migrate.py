from views import db
from _config import DATABASE_PATH

import sqlite3
from datetime import datetime
from views import app


with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()
    c.execute("DROP TABLE tasks")
    with app.app_context():
        db.create_all()
    
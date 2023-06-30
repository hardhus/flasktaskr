# project/db_create.py


from views import db, app
from models import Task
from datetime import date


# create the database and the db table
#with app.app_context():
    #db.c*reate_all()

    # instert data
    # db.session.add(Task("Finish this tutorial", date(2016, 9, 22), 10, 1))
    # db.session.add(Task("Finish Real Python", date(2016, 10, 3), 10, 1))

    # commit the changes
    #db.session.commit()
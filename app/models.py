from . import db
from datetime import datetime

class Event(db.Model):
    __tablename__='event' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(100), index=True, nullable=False)
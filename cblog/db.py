#db.py
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
import hashlib

app = Flask( __name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

class Post(db.Model):
    " post entity "
    __tablename__ = 'posts'
    id      = db.Column(db.Integer, primary_key=True)
    title   = db.Column(db.String(100))
    content = db.Column(db.Text)

    def __init__(self,title, content):
        self.title      = title
        self.content    = content

    def __repr__(self):
        return "<Post %d ,%s >" % (self.id, self.title)


def init_db():
    """ init database """
    pass

if __name__ == '__main__':
    db.drop_all()
    """ re-create tables """
    db.create_all()
    init_db()
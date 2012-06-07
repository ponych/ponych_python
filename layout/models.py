#!/usr/bin/env python

from sqlalchemy import Column, Integer, String
from hashlib import sha1
from database import Base,db_session

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nick = Column(String(50), unique= True)
    email = Column(String(120), unique=True)
    pw_hash = Column(String(40),nullable=False)

    def __init__(self,nick, email, password):
        self.nick = nick
        self.email = email
        self.pw_hash = sha1(password).hexdigest()

    def check(self,password):
        return self.pw_hash == sha1(password).hexdigest()

    def __repr__(self):
        return "<User %s %d>" % (self.nick, self.id)


def init_data():
    u = User(nick="eric",email="pony.ch@gmail.com",password="1")
    db_session.add(u)
    db_session.commit()
if __name__ == '__main__':
    Base.metadata.drop_all()
    Base.metadata.create_all()
    init_data()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#main.py
from flask import Flask,render_template as rt, abort
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from db import db
from utils import *
from views.admin import admin

app = Flask( __name__ )
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

app.register_blueprint(admin)

@app.route('/')
def index():
    return rt('index.html')

@app.route('/test/')
def test():
    return rt('test.html') ,200

if (__name__ == '__main__'):
    app.run(debug=True)


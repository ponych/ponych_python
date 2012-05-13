#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return url_for('index')

@app.route('/login/')
def login():
    return "Login"

@app.route('/user/<username>')
def profile(username):
    return "Profile"

@app.route('/test/')
def test():
    return url_for('login', next= url_for('profile',username='eric') )
    return url_for('profile',username = 'eric')


if (__name__ == '__main__'):
    app.run(debug=True)
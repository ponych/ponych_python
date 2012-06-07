#!/usr/bin/env python
from flask import Blueprint,session, request, redirect, url_for, render_template as rt
from functools import wraps
from models import *
__author__ = 'eric'

fe = Blueprint('frontend',__name__)

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for('frontend.login',next=request.url))
        return f(*args, **kwargs)
    return wrapper

@fe.route('/')
@login_required
def index():
    user = session.get('user',None)
    return rt('index.html', user=user)

@fe.route('/home/<int:id>')
@login_required
def home(id=None):
    return rt('home.html',id=id)


@fe.route('/login/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        u = User.query.filter(User.email==email).first()
        if u and u.check(password):
            session['user'] = u
            if request.args.get('next'):
                url = request.args.get('next')
            else:
                url = url_for('frontend.index')
            return redirect(url)
    return rt('login.html')

@fe.route('/logout/')
def logout():
    del session['user']
    return redirect( url_for('frontend.login'))

@fe.route('/about/')
def about():
    rt('about.html')
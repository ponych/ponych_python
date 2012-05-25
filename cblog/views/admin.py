#!/usr/bin/env python
#admin.py

from flask import Blueprint, jsonify

from flask import request, session, g,  redirect, url_for, render_template as rt
import logging

from utils import *

admin = Blueprint('admin', __name__, url_prefix='/admin')




@admin.route('/')
@login_required
def index():
    logging.debug('view admin.index^_^')
    return rt('admin/index.html')

@admin.route('/login/', methods=['POST','GET'])
def admin_login():
    return "do login"
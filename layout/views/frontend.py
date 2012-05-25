#!/usr/bin/env python
from flask import Blueprint, redirect, url_for, render_template as rt
__author__ = 'eric'

fe = Blueprint(__name__)

@fe.route('/')
def index():
    return rt('index.html')





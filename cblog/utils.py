#utils.py

from flask import Flask, g
from functools import wraps
import hashlib

def login_required(f):
    @wraps(f)
    def wrapped_func(*args, **kwargs):
        if g.user is None:
            return redirect( url_for('admin_login', next=request.url))
        return f(*args, **kwargs)
    return wrapped_func
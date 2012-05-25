#main.py

from flask import Flask, request, url_for, session, escape, render_template as rt
from flaskext.sqlalchemy import SQLAlchemy
from wtforms import Form, TextField, PasswordField, validators
from functools import wraps

app = Flask( __name__ )
app.config['DATABASE_URI'] = 'mysql://root:root@localhost/auth_test'
app.secret_key = 'aaddbb'

@app.route('/')
def index():
    return "index"

@app.route('/login/', methods= ['POST','GET'])
def login():
    app.logger.info('login page')
    form = Login(request.form)
    if request.method == 'POST':
        pass

    return rt('login.html', form=form)


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not user_id in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    app.run(debug=True)
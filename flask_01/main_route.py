#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import flash,Flask,url_for,request ,render_template, abort, redirect, make_response, session


app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username = session["username"])
    else:
        return redirect(url_for('login'))

@app.route('/login/', methods=['GET','POST'])
def login():
    if (request.method == 'POST'):
        return "do_Login"
    else:
        session["username"] = "Eric"
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect( url_for('test'))

@app.route('/user/<username>')
def profile(username):
    return "Profile"

@app.route('/test/')
def test():
    abort(404)
    return url_for('login', next= url_for('profile',username='eric') )
    return url_for('profile',username = 'eric')

@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template('404.html'), 404 )
    resp.headers["x-some"] = 'abc';
    return resp

@app.route('/flash/')
def flash_start():
    flash(['not' ,'a' ,'array'])
    flash("got you")
    return redirect(url_for('flash_show'))

@app.route('/flash/show/')
def flash_show():
    app.logger.debug("my debug info")
    app.logger.warning("warning 1")
    app.logger.error("A error")
    return render_template('flash_show.html')

if __name__ == '__main__':
    app.secret_key = 'defaa#$#ad'
    app.run(debug=True)
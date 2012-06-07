#!/usr/bin/env python

from flask import Flask, request, redirect, url_for, render_template as rt
from views.frontend import fe
app = Flask( __name__ )
app.secret_key = 'ddd'
app.register_blueprint(fe)

__author__ = 'eric'



if __name__ == '__main__':
    app.run(debug= True)
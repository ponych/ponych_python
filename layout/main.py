#!/usr/bin/env python

from flask import Flask, request, redirect, url_for, render_template as rt

app = Flask( __name__ )

__author__ = 'eric'



if __name__ == '__main__':
    app.run(debug= True)
#!/usr/bin/env python
#-*- coding: utf-8 -*-
#main.py

import web
from utils import *
import admin

from controllers import *

urls = (
    '/(.*)/', 'redirect' ,
    '/' ,'index' ,
    '/member/home' ,'member_home'
)

def session_hook():
    web.ctx.session = session

if __name__ == '__main__':
    app = web.application(urls,globals())

    if web.config.get('_session') is None:
        store = web.session.DiskStore('sessions')
        session = web.session.Session(app, store, initializer={'login':0,'username':''})

        web.config._session = session
    else:
        session = web.config._session

    #app.add_processor(load_sqla)
    app.add_processor(web.loadhook(session_hook))

    # run
    app.run()


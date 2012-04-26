#!/usr/bin/env python
#3main.py
import web
#import admin
from controllers import *
from proccessors import load_sqla

urls = (
    '/(.*)', 'redirect',
    '/', 'index',
    'tag/([-\w])', 'tag',
    '/category/([-\w+])', 'category',
    '/search', 'search',
    '([-\w]+)','singlepost',
)

app = web.application(urls,globals(), autoreload=True)


# tips: to fix the problem that session can't work at Debug mode
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'login':0, 'username':'',})
    web.config._session = session
else:
    session = web.config._session


# make session available in sub-apps
def session_hook():
    web.ctx.session = session

app.add_proccessor(load_sqla)
app.add_proccessor(web.loadhook(session_hook))

if __name__ == '__main__':
    app.run()

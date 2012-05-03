#!/usr/bin/env python
#3main.py
import web
import admin
#from controllers import *
from proccessors import load_sqla
from controllers import *

urls = (
    # '/(.*)', 'redirect',
    '/', 'index',
    '/admin' ,admin.app_admin,
#    'tag/([-\w])', 'tag',
#    '/category/([-\w+])', 'category',
#    '/search', 'search',
 #   '([-\w]+)','singlepost',
    '/archive/([-\w]+)' , "singlepost"
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

class redirect:
    """docstring for redirect"""
    def GET(self, path):
        web.seeother('/'+path)
        

app.add_processor(load_sqla)
app.add_processor(web.loadhook(session_hook))

# can be customize
app.notfound = notfound

if __name__ == '__main__':
    app.run()

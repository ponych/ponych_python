#!/usr/bin/env python
#-*- coding:utf-8 -*-
#controllers.py

import web
from utils import *

from member import *

class redirect:
    def GET(self, path):
        web.seeother('/'+path)

class index:
    def GET(self):
        return render.index()


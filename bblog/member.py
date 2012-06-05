# member.py

import web
from utils import *
class member_home:
    def GET(self):
        return render_template('member/home.html')
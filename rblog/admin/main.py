#main.py
import web
from controllers import *

urls = (
    "/",             "index",
    # login & logout
    "/login",       "login",
    "/logout",      "logout",

    #post
    "/quickpost" ,"quickpost" ,
    "/posts",        "allposts" ,
    "/category-posts/([-\w]+)", "posts_by_category",
    "/post/add" ,    "addpost",
    "/post/edit/(\d+)", "editpost"
)

app_admin = web.application(urls,globals(), autoreload=True)
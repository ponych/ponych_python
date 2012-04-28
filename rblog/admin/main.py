#main.py
import web
from controllers import *

urls = (
    "",             "index",
    # login & logout
    "/login",       "login",
    "/logout",      "logout",

    #post
    #"/quickpost" ,"quickpost" ,
    "posts",        "allposts" ,
    "category-posts/([-\w]+)", "posts_by_category",
    "post/add" ,    "addpost",
    "post/edit/(\d+)", "editpost"
)

appp_main = web.applcation(urls,globals(), autoreload=True)
#controllers.py
import web
from sqlalchemy import and_, or_, extract
from markdown import markdown

from models import *
from config import render, render_template
from config import POST_PER_PAGE
from forms  import comment_form
# from akismet import Aksimet, AkismetError, APIKeyError

import sidebar

#function class start here
def get_sidebar():
    return { 
        'page'      : sidebar.pages(),
        'category'  : sidebar.categories(),
        'tags'      : sidebar.tags(),
        'links'     : sidebar.links(),
        'recentcomments': sidebar.recentcomments(),
        'archives'  : sidebar.archives()
    }


def notfound():
    return web.notfound(render.notfound())
    # can also use template result like below,ehter is ok
    # reutrn web.notfound(render.notfound())
    # return web.notfound(str(render.notfound()))


class index():
    """docstring for index"""
    def GET(self):
        i = web.input(page=1)
        try:
            page = int(i.page)
        except:
            page = 1

        context = {}

        post_count = web.ctx.orm.query(Post).\
                                 filter(Post.content_type=='post').count()

        page_count = post_count / POST_PER_PAGE
        if post_count % POST_PER_PAGE != 0:
            page_count += 1
        
        context['widget']       = get_sidebar()
        context['page_count']   = page_count
        context['posts']        = web.ctx.orm.query(Post)
        context['page']         = page
        context['location']     = 'home'

        return render_template('index.html' , **context)

class singlepost:
    """docstring for singlepost"""
    def get_post_by_slug(self, slug):
        post = web.ctx.orm.query(Post).\
                           filter(Post.slug==slug).first()
        if post:
            return post
        else:
            return None

    def get_post_by_id(self, id):
        post = web.ctx.orm.query(Post).\
                           filter(Post.id==id).first()
        if post:
            return post
        else:
            return None
    
    def get_post(self, arg):
        try:
            arg = int(arg)
            post = self.get_post_by_id(arg)
        except:
            post = self.get_post_by_slug(arg)
        return post

    #def validate_comment(self, comment):

    def GET(self, arg):
        post = self.get_post(arg)

        f = comment_form()
        if post:
            post.view_count += 1
            widget = get_sidebar()
            widget['relative_posts'] = sidebar.relative_posts(post)
            return render_template('single.html', form=f,
                                                admin = web.ctx.session.username,
                                                post= post,
                                                widget=widget,
                                                location= 'single')
        else:
            raise web.notfound

    def POST(self,arg):
        post = self.get_post(arg)
        f = comment_form()

        if post:
            if f.validates():
                #store comment
                comment = Comment(
                    author  = f.author.value,
                    email   = f.email.value,
                    url     = f.url.value,
                    content = f.comment.value,
                    ip = web.ctx.get('ip', '') ,
                    post_id = post.id
                )

                web.ctx.orm.add(comment)
                post.comment_count += 1
                web.ctx.orm.commit()
                web.seeother(comment.get_absolute_url())
            else:
                return render.single(post=post, widget=get_sidebar(),form = f,location='single')
        else:
            raise web.notfound

# class category:
#     """docstring for category"""
#     def GET(self, arg):

        

        
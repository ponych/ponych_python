#!/usr/bin/env python
#-*- coding:utf-8 -*-
#controllers.py
#import math
import web
import hashlib
from datetime import datetime
from markdown import markdown
from sqlalchemy import extract

from config import admin_render, render_template
from config import ADMIN_POST_PER_PAGE, ADMIN_COMMENT_PER_PAGE
from models import *
from sidebar import archives
from forms import settings_form
from admin.utils import post_slug_validates, term_slug_validates

# a decorator

def login_required(func):
    def function(*args):
        if web.ctx.session.login == 0:
            raise web.seeother("/login")
        else:
            return func(*args)

    return function


class login(object):
    """ login """
    def GET(self):
        return admin_render.login()

    def POST(self):
        i = web.input(name=None,passowrd=None)

        message = "username or password is nul!"
        print i.name
        if i.name and i.password:
            admin = web.ctx.orm.query(User).filter(User.name==i.name).first()
            if admin:
                if hashlib.md5(i.password).hexdigest() == admin.password:
                    web.ctx.session.login   = 1
                    web.ctx.session.admin   = admin
                    web.ctx.session.uid     = admin.id
                    web.ctx.session.username = admin.name
                    web.ctx.session.email   = admin.email
                    raise web.seeother("/")
                else:
                    message  = "Wrong passowrd!"
            else:
                message = "User not exists"

        return admin_render.login(message=message)

class logout(object):
    def GET(self):
        web.ctx.session.kill()
        raise web.seeother("/login")

class index(object):
    """ index """
    @login_required
    def GET(self):
        context = {}

        context['post_count'] = web.ctx.orm.query(Post).\
                                            filter(Post.content_type=="post").count()
        # context['comment_count'] = web.ctx.orm.query(Comment).count()
        # # context['spam_count']
        # context['category_count']   = web.ctx.orm.query(Term).filter(Term.type=='category')
        # context['tag_count'] = web.ctx.orm.query(Term).filter(Term.type=='tag')
        # context['recent_comments'] = web.ctx.orm.query(Comment).order_by('comments.created DESC').all[:5]

        return admin_render.index(**context)

class quickpost(object):
    @login_required
    def POST(self):
        i       = web.input()
        title   = i.title.strip()
        content = i.content.strip()
        tags    = i.tags.strip()

        if not (title and content):
            return "<p style=\"color:red\">Title and content can not be empty</p>"

        post = Post(title=title, content=content, author=web.ctx.session.admin)
        for item in tags.split(','):
            tag = web.ctx.orm.query(Term).filter(Term.type=='tag').filter(Term.name==item.strip()).first()

            if not tag:
                tag = Term(name=item.strip(),type='tag', count=0)
                web.ctx.orm.add(tag)

            tag.count += 1
            post.terms.append(tag)

        if i.get('publish', ''):
            post.status = 'publish'
        else:
            post.status = 'draft'

        web.ctx.orm.add(post)
        web.ctx.orm.commit()
        return "<p>Post has been saved</p>"

class allposts(object):
    def all_count(self):
        return web.ctx.orm.query(Post).filter(Post.content_type=='post').count()

    def pub_count(self):
        return web.ctx.orm.query(Post).filter(Post.content_type=='post').\
                                      filter(Post.status=='publish').count()
    
    @login_required
    def GET(self):
        i = web.input(page=1)
        try:
            page = int(i.page)
        except:
            page = 1

        context = {'page': page}


        query = web.ctx.orm.query(Post).filter(Post.content_type=="post")

        if i.get('status',''):
            query = query.filter(Post.status==i.status)
            context['status'] = i.status
        
        post_count = query.count()

        posts = query.order_by('posts.created DESC').all()

        page_count = max( post_count / ADMIN_POST_PER_PAGE ,0)

        if post_count % ADMIN_POST_PER_PAGE > 0: # for not same
            page_count +=1

        context['posts'] = posts[(page-1)*ADMIN_POST_PER_PAGE:ADMIN_POST_PER_PAGE*page]
        context['all_count'] = self.all_count()
        context['page_count'] = page_count
        context['publish_count'] = self.pub_count()
        context['draft_count'] = web.ctx.orm.query(Post).filter(Post.status=='draft').count()
        context['categories']   = web.ctx.orm.query(Term).filter(Term.type=='category').all()
        context['archives'] = archives()


        return admin_render.posts(**context)

class addpost(object):
    """docstring for addpost"""
    @login_required
    def GET(self):
        cates = web.ctx.orm.query(Term).filter(Term.type='category').all()
        return admin_render.addpost(cates =cates, action='add', content_type='post')
    
    @login_required
    def POST(self):
        i = web.input(category=[])
        title = i.title
        slug = None
        if i.slug.strip():
            slug = i.slug.strip().replace(' ','-')

        excerpt = i.excerpt
        tags = i.tags
        



        
        

        
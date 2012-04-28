#!/usr/bin/env python
#sidebar.py
import web
from sqlalchemy import func, extract
from models import Post, Term, Link, Comment

# get page
def pages():
    pages = web.ctx.orm.query(Post).filter(Post.content_type=='page').\
                                    filter(Post.status=="publish").\
                                    order_by("posts.menu_order DESC")

    return pages


# getcategories
def categories():
    return web.ctx.orm.query(Term).filter(Term.type=='category').all()

# get tags
def tags(count=25):
    return web.ctx.orm.query(Term).filter(Term.type=='tag').\
                                   order_by('terms.count DESC')[:count]

#get links
def links():
    return web.ctx.orm.query(Link).all()

def recentcomments(count=7):
    return web.ctx.orm.query(Comment).filter(Comment.status=='approved').\
                                      order_by('comments.created DESC')[:count]

def archives():
    archive = web.ctx.orm.query(
        extract('month', Post.created).label('month'),
        Post.created,
        func.count('*').label('count')
    ).filter(Post.content_type=='post').group_by('month').all()

    ret = []
    for month, date, count in archive:
        d = {}
        d['date'] = date
        d['count'] = count
        ret.append(d)

    return ret

def relative_posts(post,count=7):
    """ get relative posts, saying thes post with the same tag"""

    tags = []

    for term in post.terms:
        if term.type=='tag':
            tags.append(term.id)

    posts = web.ctx.orm.query(Post).filter(Post.terms.any(Term.id.in_(tags)))

    if posts:
        posts = posts.filter(Post.id != post.id).all()[:count]
    return posts








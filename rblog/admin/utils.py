#!/usr/bin/env python
#-*- coding:utf-8 -*-
# utils.py

import web
from sqlalchemy import func, extract
from models import Post,Term

def post_slug_validates(slug,id=None):
    if not id:
        count = web.ctx.orm.query(Post).filter_by(slug=slug).count()
    else:
        count = web.ctx.orm.query(Post).filter(Post.id!=id).\
                                        filter(Post.slug==slug).count()

    return count ==0


def term_slug_validates(slug, id=None):
    if not id:
        count = web.ctx.orm.query(Term).filter_by(slug=slug).count()
    else:
        count = web.ctx.orm.query(Term).filter(Term.id!=id).filter(Term.slug==slug).count()

    return count == 0
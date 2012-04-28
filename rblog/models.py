#!/usr/bin/env python
#-*-coding:utf-8-*-
# models.py

import web
import hashlib
from datetime import datetime

from sqlalchemy import create_engine,Table ,ForeignKey
from sqlalchemy import Column,Integer,String,Text,DateTime
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker, relationship,backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:root@localhost/rblog?charset=utf8', echo=True)
# engine = create_engine('sqlite://rblog.db', echo=True)
Base = declarative_base()

# for the many-to-many relationships between Post and Term
term_relationships = Table('term_relationships', Base.metadata, 
        Column('post_id', Integer, ForeignKey('posts.id')),
        Column('term_id', Integer,ForeignKey('terms.id'))
    )

class Post(Base):
    """ can be a post or page """
    __tablename__ = 'posts'

    id             = Column(Integer(6), primary_key=True)
    author_id      = Column(Integer(6), ForeignKey('users.id') )
    title          = Column(String(64), nullable=False)
    slug           = Column(String(64),unique=True)
    excerpt        = Column(Text)
    content        = Column(Text)
    content_type   =  Column(String(10), default='post') # post || page
    status         = Column(String(10), default='publish') # publish, draft
    created        = Column(DateTime,      default=datetime.now)
    modified    = Column(DateTime,   default=datetime.now)
    comment_status= Column(Integer(1), default= 1) # 1:allow to comment,0: not
    comment_count = Column(Integer(4), default= 0) #
    view_count  = Column(Integer(6) ,default = 0)
    menu_order     = Column(Integer(3) , default= 0)
    link         = Column(String(255), unique=True)

    author = relationship('User',backref=backref('posts', lazy='dynamic'))

    terms = relationship('Term', secondary=term_relationships,
        backref=backref('posts',lazy='dynamic'))

    def __repr__(self):
        return "<Post (%s)>" % str(self.id)

    def get_absolute_url(self):
        if self.slug:
            s = self.slug
        else:
            s = str(self.id)

        if self.content_type == 'post': 
            base_url = "/archive/%s"
        else:
            base_url = "/%s"

        return base_url % s

    def shortcontent(self, length=3000):
        return self.content[:length]

    def get_next(self):
        posts = web.ctx.orm.query(Post).\
                                       filter(Post.content_type=='post').\
                                       filter(Post.status=='publish').\
                                       filter('created>:time').params(time=self.created).\
                                       order_by('created').all()
        
        if len(posts) > 0:
            return posts[0]
        else:
            return None

    def get_prev(self):
        posts = web.ctx.orm.query(Post).\
                            filter(and_(Post.content_type=='post', Post.status=='publish')).\
                            filter("created<:time").params(time=self.created).\
                            order_by('created').all()
        if len(posts) > 0:
            return posts[-1]
        else:
            return None

class User(Base):
    __tablename__ = 'users'

    id         = Column(Integer(6), primary_key=True)
    name     = Column(String(64), nullable=False, unique=True)
    password= Column(String(255), nullable=False)
    email   = Column(String(255), nullable=False, unique=True)
    url     = Column(String(255))

    def __repr__(self):
        return "<User (%s)>" % self.name


class Term(Base):
    """category or tag """
    
    __tablename__ = 'terms'

    id         = Column(Integer(5), primary_key=True)
    name    = Column(String(64), nullable=False)
    slug    = Column(String(64), unique=True, nullable=True)
    description = Column(String(255))
    type    = Column(String(10), default='tag') # tag || category
    count   = Column(Integer(6), default=0)
    order   = Column(Integer(5), default=0)

    def __repr__(self):
        return "<Term (%s)>" % self.id

    def get_absolute_url(self):
        if self.slug:
            s = self.slug
        else:
            s = str(self.id)
        
        return "/%s/%s" % (self.type , s)

class Comment(Base):
    """docstring for Comment"""
    __tablename__ = 'comments'

    id         = Column(Integer(8), primary_key=True)
    post_id = Column(Integer(6), ForeignKey('posts.id'))
    author  = Column(String(64), nullable=False)
    email   = Column(String(64), nullable=False)
    url     = Column(String(255))
    ip         = Column(String(40))
    created    = Column(DateTime,      default=datetime.now)
    content = Column(Text)
    status  = Column(String(10),default='aproved') # aproved,spam,waiting
    parent_id = Column(Integer(8),ForeignKey('comments.id'))

    # many-to-one relation Comment <-> Post
    post = relationship('Post',backref=backref('comments',order_by=created))

    #many-to-one Comment <-> Comment
    parent = relationship('Comment', 
                          backref=backref('children',remote_side=[id],order_by=created)
                        )

    def __repr__(self):
        return "<Comment (%s)>" % str(self.id)

    def get_absolute_url(self):
        return self.post.get_absolute_url()+("#comment-%d" % self.id)

class Option(Base):
    """ options for this blog """
    __tablename__ = 'options'

    id         = Column(Integer(4), primary_key=True)
    name    = Column(String(64), unique=True)
    autoload= Column(Integer(1), default=1) # 1: yes, 0:no

    def __repr__(self):
        return "<Option (%s)>" % self.name

class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    url = Column(String(255))
    description = Column(String(255))

    def __repr__(self):
        return "<Link (%d)>" % self.id

def init_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    cate = Term(name='Uncategory', slug='uncategory',type='category')
    session.add(cate)

    pw = hashlib.md5(u'123456').hexdigest()
    user = User(name='eric', password=pw, email="pony.ch@gmail")
    session.add(user)

    post = Post(title="First Post test!",content="Hello,World",author=user)
    post.terms.append(cate)
    session.add(post)

    session.commit()
    session.close()


if __name__ == '__main__':
    Base.metadata.drop_all(engine) # delete tables before
    Base.metadata.create_all(engine) # create all tables
    init_db() # init data

        



        


        








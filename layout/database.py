#!/usr/bin/env pytnon

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:root@localhost/')
__author__ = 'eric'

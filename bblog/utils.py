#!/usr/bin/env python
#-*- coding: utf-8 -*-
#utils.py

import os
import web
from web.contrib.template import render_jinja
from jinja2 import Environment, FileSystemLoader

POST_PER_PAGE = 5
ADMIN_POST_PAGE = 7


def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'tpl')),
            extensions=extensions,
            )
    jinja_env.globals.update(globals)

    #jinja_env.update_template_context(context)
    return jinja_env.get_template(template_name).render(context)
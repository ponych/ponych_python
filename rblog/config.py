# config.py

__all__ = [
    "POST_PER_PAGE", "ADMNI_POST_PER_PAGE", "ADMIN_COMMENT_PER_PAGE",
    "render", "admin_render" ,
    "render_template"
]

import os
import web
import cgi
from web.contrib.template import render_jinja
from jinja2 import Environment, FileSystemLoader

POST_PER_PAGE           = 5
ADMNI_POST_PER_PAGE     = 7
ADMIN_COMMENT_PER_PAGE  = 9

cgi.maxlen = 5 * 1024 * 1024 # POST maxlen 5M

def getRender():
    render = render_jinja(
        'tpl',
        encoding = 'utf-8'
    )

    return render

def getAdminRender():
    render = render_jinja(
        'tppl/admin',
        encoding = 'utf-8'
    )

    return render

render          = getRender()
admin_render    = getAdminRender()

# implement "read more..." feature
def post_excerpt(post):
    end = post.find('<!-- pagebreak -->') # find <!-- agebreak -->

    if end == -1:
        return post
    else:
        return post[:end]

# render templete with specific template name

def render_template(template_name ,**context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', [])

    jinja_env = Environment(
        loader = FileSystemLoader(os.path.join(os.path.dirname(__file__),'tpl')),
        extensions=extensions
    )

    jinja_env.globals.update(globals)
    jinja_env.filters['excerpt'] = post_excerpt

    #jinja_env.update_template_context(context)
    return jinja_env.get_template(template_name).render(context)


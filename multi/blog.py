#blog.py
import web

urls = (
	'' ,"reblog" ,
	'/(.*)', "blog"
)

class reblog:
	def GET(self):
		raise web.seeother("/"+'no_blog')

class blog:
	def GET(self, path):
		return "blog "+ path

app_blog = web.application(urls ,locals())
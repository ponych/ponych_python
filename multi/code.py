#code.py
import web
import blog
urls = (
	'/blog', blog.app_blog,
	'/(.*)', "index"
)

class index:
	def GET(self,path):
		return "Hello,"+path

app = web.application(urls,locals())

if __name__ == '__main__':
	app.run()
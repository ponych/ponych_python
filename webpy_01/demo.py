import web

urls = (
	'/(.*)', 'hello'
)

class hello:
	def GET(self, name):
		if not name:
			name = 'World'
		render = web.template.render('tpl/')

		return render.index(name)

if '__main__' == __name__:
	app = web.application(urls, globals())
	app.run()
# coding: utf8
import web
import model


### todo.py url mappings

urls = (
	'/', 'Index' ,
	'/del/(\d+)', 'Delete'
)

### Templates
render = web.template.render('tpl', base='base')

class Index:
	form = web.form.Form(
	    web.form.Textbox('title', web.form.notnull, description="I need to要做的事情:"),
		web.form.Button('Add todo')
	)
	def GET(self):
		" Show page of todos"
		todos = model.get_todos()
		form  = self.form()
		return render.index(todos, form)

	def POST(self):
		" Add new entry "
		form = self.form()

		if (not form.validates()):
			return self.GET(self)

		model.new_todo(form.d.title)

		raise web.seeother('/')

class Delete:
	def POST(self, id):
		"Delete based on ID "
		id = int(id)
		model.del_todo(id)
		raise web.seeother('/')

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
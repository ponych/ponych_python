# coding: utf8
import web
import model


urls = (
	'/', 'Index' ,
	'/view/(\d+)', 'View',
	'/new' , 'New',
	'/delete/(\d+)', 'Delete',
	'/edit/(\d+)', 'Edit'
)

t_globals = {
	'datestr': web.datestr
}

render = web.template.render('tpl', base='base', globals=t_globals)

class Index:
	def GET(self):
		posts = model.get_posts()
		return render.index(posts)

class View:
	def GET(self,id):
		post = model.get_post(int(id))
		return render.view(post)

class New:
	form = web.form.Form(
		web.form.Textbox('title',web.form.notnull,size=30, description='标题必填'),
		web.form.Textarea('content', web.form.notnull,rows=30,cols=20),
		web.form.Button('Post Entry')
	)
	
	def GET(self):
		form = self.form()
		return render.new(form)

	def POST(self):
		form = self.form()
		if not form.validates():
			return render.new(form)

		model.new_post(form.d.title,form.d.content)

		raise web.seeother('/')

class Delete:
	def POST(self, id):
		model.del_post(int(id))
		raise web.seeother('/')

class Edit:
	def GET(self, id):
		post = model.get_post(int(id))
		form = New.form()
		form.fill(post)

		return render.edit(post, form)

	def POST(self, id):
		form = New.form()
		post = model.get_post(int(id))

		if not form.validates():
			return render.edit(form, post)

		model.update_post(int(id), form.d.title, form.d.content)

		raise web.seeother('/view/'+str(post.id))


if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
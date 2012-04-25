import web, datetime

db = web.database(dbn='mysql',db='python',user='root',pw='root')

def get_posts():
	return db.select('blog_entries', order='id DESC')

def get_post(id):
	try:
		return db.select('blog_entries',where='id=$id',vars=locals())[0]
	except IndexError:
		return none

def new_post(title, text):
	db.insert('blog_entries',title=title, content=text, posted_on=datetime.datetime.utcnow())

def del_post(id):
	db.delete('blog_entries', where='id=$id', vars=locals())

def update_post(id, title, text):
	db.update('blog_entries', where='id=$id', vars=locals(), title=title, content=text)


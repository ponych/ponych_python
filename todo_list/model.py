import web

db = web.database(dbn='mysql', user='root', pw='root', db='python')

def get_todos():
	return db.select('todo', order='id')

def new_todo(text):
	db.insert('todo', title=text)

def del_todo(id):
	db.delete('todo', where="id=$id", vars=locals())

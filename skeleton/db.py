import config

def listing(**k):
	return config.db.select('items',**k)
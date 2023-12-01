from bottle import route, run

@route('/<name>')
def index(name='World'):
	return 'Hello %s!' % name

run(host='localhost', port=8080)

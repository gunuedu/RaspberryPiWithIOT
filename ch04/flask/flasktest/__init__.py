from flask import Flask, request, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/object/<int:id>')
def callback(id):
    assert isinstance(id, int)
    return url_for('callback', id=id)

@app.route('/login', methods=['GET'])
def show_loginform():
    return '''
        <form action="/login" method="post">
            Username : <input name="username" type="text" />
            Password : <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

def check_login(username, password):
    if username=="pi" and password=="raspberry":
        return True
    else:
        return False

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

@app.route('/question', methods=['GET'])
def question():
   return request.args.get('answer')

@app.route('/question', methods=['POST'])
def form_question():
    return request.form.get('answer')

@app.route('/questionall', methods=['GET', 'POST'])
def question_all():
	return request.values.get('answer')

@app.route('/json', methods=['POST'])
def json():
   print(request.get_json())
   return str(request.get_json())

@app.route('/path', methods=['GET', 'POST'])
def get_path():
   return ("path: %s<br>"
      "script_root: %s<br>"
      "url: %s<br>"
      "base_url: %s<br>"
      "url_root: %s<br>") % (request.path, request.script_root,
         request.url, request.base_url, request.url_root)

from flask import Response
@app.route('/response')
def custom_response():
   resp = Response("응답 테스트")
   resp.headers.add('Text-Name', 'Response Test')
   resp.set_data('이것은 응답 테스트입니다')
   return resp

from flask import redirect
@app.route('/hi')
def hi():
  return  redirect("/hello")

@app.route('/hello')
def hi_hello():
  return  "Hello"

@app.errorhandler(404)
def error404(error):
  return "이 페이지는 존재하지 않습니다."

from flask import abort
@app.route('/wrong')
def wrong():
   abort(401, "죄송합니다. 이 페이지는 존재하지 않습니다.")

from flask import make_response
@app.route('/cookie')
def hello_again():
   if request.cookies.get("visited"):
      return "Welcome back! Nice to see you again"
   else:
      response = make_response("Hello there! Nice to meet you")
      response.set_cookie("visited", "yes")
      return response


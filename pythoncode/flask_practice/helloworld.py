from flask import Flask
from flask import request


app = Flask(__name__) 
#Name argument that is passed to the Flask application constructor is a source of confusion. Flask
# use this argument to determine the root path of the application so that is later can find resource files relative to
# the location of the application

@app.route('/')
def index():
    return '<h1>hello world</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>hello %s!</h1>' %name

# request object is available in the context where your app is running and is globally accessible for every view
# function. 
# There are two contexts in flask, Application context and request context. 
# Each thread has it own context
@app.route('/browser')
def info():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s<p>' % user_agent


if __name__ == '__main__':
    app.run(debug=True)

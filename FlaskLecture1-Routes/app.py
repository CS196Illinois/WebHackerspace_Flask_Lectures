from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	return "<h1> Hello World! </h1>"

@app.route('/user/<name>')
def user(name):
	return "<h1> Hello %s!</h1>" % name

@app.route('/user2/<name>')
def user2(name):
     return render_template('index.html', name=name)

if __name__ == '__main__':
	app.run(debug=True)

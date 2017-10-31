from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	return "<h1> Hello World! </h1>"

@app.route('/route1/<int:post_id>')
def route1(post_id):
    return 'Route 1 Number %d' % post_id

@app.route('/route2/<name>')
def route2(name):
     return render_template('index.html', name=name)

if __name__ == '__main__':
	app.run(debug=True)

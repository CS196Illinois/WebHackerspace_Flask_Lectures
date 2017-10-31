# Flask Routes

This creates an application instance
__name__ is used to determine the root path of the application folder

```python
from flask import Flask
app = Flask(__name__)
```

Running the Server

```python
if __name__ == '__main__':
	app.run(debug=True)
```

App routes define the path to different pages in your application 
```python
@app.route('/')
def index():
	return "Hello World!"
```

The return statement has to be a string or be rendering a template. A template contains the HTML necessary to render the page correctly. 

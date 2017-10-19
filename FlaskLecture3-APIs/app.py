from flask import Flask, request, render_template
import wikipedia
import urllib.request
import json
from twitter import *


app = Flask(__name__)	

@app.route('/search/<input>')
def main(input):
    return "This is your assignment, fill this in"

app.run(debug=True)

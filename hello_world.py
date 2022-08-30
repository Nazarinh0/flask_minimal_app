from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/99-bottles')
def index():
    return render_template(
        'index.html',
	title='BOTTLES',
	numbers=range(99, 0, -1),
        )


@app.route('/args')
def argument():
    return render_template(
        'args.html',
        arg=request.args.lists(),
        )


@app.route('/json')
def json():
    return dict(request.args.lists())

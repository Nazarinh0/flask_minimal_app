from flask import Flask
from flask import render_template

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

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Heipparallaa!"

@app.route("/page1")
def page1():
	return "Eka sivu"

@app.route("/page2")
def page2():
	return "Toka sivu"

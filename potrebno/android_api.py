import flask, json
from flask import Flask, request

app = Flask('__main__', template_folder="", static_folder="", root_path="", static_url_path="")
msgs = []

@app.route('/')
def index_page():
    return ("Hello")

@app.route('/users')
def korisnici():
    return flask.send_file("users.json")

@app.route('/json/<number>')
def prikaz_jednog(number=None):
    try:
        with open("monsters.json") as f:
            data = json.load(f)
            n = int(number)
            return str(data[n])
    except(Exception):
        return "Greška"

@app.route('/json')
def ret_json():
    return flask.send_file("monsters.json")
app.run("0.0.0.0", 5000)

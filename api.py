import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return "<h1>Jeopardy API</h1><p>Simple REST API to return random Jeopardy clues used in past games.</p>"

@app.route('/api/v1/jeopardy/questions/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('./jeopardy.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM questions;').fetchall()

    return jsonify(all_books)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><br /><p>The resource could not be found.</p>", 404

app.run()

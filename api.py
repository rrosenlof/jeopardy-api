import flask
from flask import request, jsonify
import sqlite3
from random import randrange

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

# @app.route('/api/v1/jeopardy/questions/all', methods=['GET'])
# def api_all():
#     conn = sqlite3.connect('./j.db')
#     conn.row_factory = dict_factory
#     cur = conn.cursor()
#     all_qs = cur.execute('SELECT * FROM questions;').fetchall()
#     return jsonify(all_qs)

@app.route('/api/v1/jeopardy/questions/random', methods=['GET'])
def api_random():
    conn = sqlite3.connect('./j.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    count = cur.execute('SELECT COUNT(*) as count FROM questions;').fetchone()
    rand_index = str(randrange(1,count['count']))
    query = 'SELECT * FROM questions where id=?;'
    random = cur.execute(query,[rand_index]).fetchone()
    return jsonify(random)

@app.route('/api/v1/jeopardy/categories/random', methods=['GET'])
def api_random_full_cat():
    conn = sqlite3.connect('./j.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    count = cur.execute('SELECT COUNT(cat_id) as count FROM questions;').fetchone()
    rand_index = str(randrange(1,count['count']))
    query = 'SELECT * FROM questions where id=?;'
    random = cur.execute(query,[rand_index]).fetchone()
    return jsonify(random)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><br /><p>The resource could not be found.</p>", 404

app.run()

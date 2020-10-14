import flask
from flask import request, jsonify
import sqlite3
from random import randrange

app = flask.Flask(__name__)
app.config["DEBUG"] = False

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return "<h1>Jeopardy REST API</h1><p>Simple REST API to return random Jeopardy clues used in past games.</p>"

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
    cat_ids = cur.execute('select distinct cat_id from questions where full_category is \'TRUE\';').fetchall()
    max_id = len(cat_ids)
    rand_index = randrange(1,max_id)
    rand_cat_id = cat_ids[rand_index]['cat_id']
    query = 'SELECT * FROM questions where cat_id=?;'
    random = cur.execute(query,[rand_cat_id]).fetchall()
    return jsonify(random)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><br /><p>The resource could not be found.</p>", 404

app.run()

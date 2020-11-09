"""API"""

from flask import Flask, request, jsonify
from main import Database

app = Flask(__name__)


@app.route('/', methods=['POST'])
def insert():
    """Call to insert function."""
    insert_name = request.args.get('name')
    insert_uname = request.args.get('username')
    insert_email = request.args.get('email')
    insert_URL = request.args.get('url')
    insert_Tags = request.args.get('tags')
    result = jsonify(Database().insert_info(insert_name, insert_uname, insert_email, insert_URL, insert_Tags))
    return result


@app.route('/', methods=['GET'])
def search():
    """Call to search function."""
    search_name = request.args.get('name')
    result = jsonify(Database().search_database(search_name))
    return result


@app.route('/', methods=['DELETE'])
def delete():
    """Call to delete function."""
    delete_name = request.args.get('name')
    result = jsonify(Database().delete_info(delete_name))
    return result


@app.route('/', methods=["PATCH"])
def update():
    changes = request.get_json()
    username = request.args.get('name')
    return jsonify(Database().update_database(username, changes))


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response


if __name__ == '__main__':
    app.run(debug=1)

"""API"""

from flask import Flask, request, jsonify
from main import Database

app = Flask(__name__)


@app.route('/', methods=['POST'])
def insert():
    """Call to insert function."""
    json_passed = request.get_json()
    insert_name = json_passed.get('name')
    insert_uname = json_passed.get('username')
    insert_email = json_passed.get('email')
    insert_URL = json_passed.get('url')
    insert_Tags = json_passed.get('tags')
    result = jsonify(Database().insert_info(insert_name, insert_uname, insert_email, insert_URL, insert_Tags))
    return result


@app.route('/', methods=['GET'])
def get_entries():
    """Call to search function."""
    result = jsonify(Database().get_info())
    return result


@app.route('/', methods=["GET"])
def search():
    name = request.args.get("name")
    return jsonify(Database().search_database(name))


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
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,PATCH')
    return response


if __name__ == '__main__':
    app.run(debug=1)

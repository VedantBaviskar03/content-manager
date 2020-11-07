"""API"""

from flask import Flask, request, jsonify
from main import Database

app = Flask(__name__)


@app.route('/', methods=['POST'])
def insert():
    """Call to insert function."""
    insert_name = request.args.get('name')
    insert_URL = request.args.get('url')
    insert_Tags = request.args.get('tags')
    result = jsonify(Database.insert_info(insert_name, insert_URL, insert_Tags))

@app.route('/', methods=['GET'])
def search():
    """Call to search function."""
    search_name = request.args.get('name??')
    result = jsonify(Database.search_database(search_name))
    return result


@app.route('/', methods=['POST'])
def delete():
    """Call to delete function."""
    delete_name = request.args.get('name')
    result = jsonify(Database.delete_info(delete_name))


if __name__ == '__main__':
    app.run(debug=1)

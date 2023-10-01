#!/usr/bin/python3
'''
Module: contains the main application
'''
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(obj):
    ''' calls close() method '''
    storage.close()


@app.errorhandler(404)
def handle_api_error(exception):
    '''
    Returns a JSON-formatted 404 status code respose
    '''
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host, int(port), threaded=True)

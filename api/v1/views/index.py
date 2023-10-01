#!/usr/bin/python3
'''
index - index page to run api
'''
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    '''
    Returns a JSON status
    '''
    return jsonify({"status": "OK"})

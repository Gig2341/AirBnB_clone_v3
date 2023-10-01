#!/usr/bin/python3
'''
Retrieves, creates, updates and deletes all states objects
as well as with state.id if exists.
'''
from api.v1.views import app_views
from flask import (abort, jsonify, make_response, redirect,
                   request, url_for)
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def states():
    ''' Retrieves the list of all State objects on GET
    Creates a State on POST.
    '''

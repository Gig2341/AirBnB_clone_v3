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
    if request.method == 'GET':
        objs = storage.all(State)
        all_states = [obj.to_dict() for obj in objs.values()]
        return jsonify(all_states)

    if request.method == 'POST':
        state_obj = request.get_json()
        if state_obj is None:
            abort(400, "Not a JSON")
        if state_obj.get('name') is None:
            abort(400, "Missing name")
        new_state = State(**state_obj)
        new_state.save()
        return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def state_id(state_id):
    ''' Retrieves a state obj on GET request.
    Deletes a state obj on POST request.
    '''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(state.to_dict())

    if request.method == 'DELETE':
        state.delete()
        storage.save()
        return make_response(jsonify({}), 200)

    if request.method == 'PUT':
        state_obj = request.get_json()
        if state_obj is None:
            abort(400, 'Not a JSON')
        for k, v in state_obj.items():
            if k not in ['id', 'created_at', 'updated_at']:
                setattr(state, k, v)
        storage.save()
        return jsonify(state.to_dict())

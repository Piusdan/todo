#!flask/bin/python

"""
Views for the todo application
"""
from flask import jsonify, abort, request, json, redirect, url_for
from .. import db
from ..models import Todo
from ..schemas import todo_schema, todos_schema
from . import api


@api.route('/todos', methods=['GET'])
def get_todos():

    """
    get all todo items
    """
    all_todos = Todo.query.all()
    return todos_schema.jsonify(all_todos), 201


@api.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):

    """
    gets a single todo item referenced by the todo id
    """
    todo = Todo.query.filter_by(id=todo_id).first_or_404()
    return todo_schema.jsonify(todo), 201


@api.route('/todos', methods=['POST'])
def create_todo():

    """
    creates a new todo item
    """
    title = request.json.get('title', '')
    todo = Todo(title)
    if todo:
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('get_todos'))
    else:
        return jsonify({'message': 'failed'})


@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """
    Deletes a todo item
    """

    todo = Todo.query.filter_by(id=todo_id).first_or_404()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('get_todos'))


@api.route('/todos/complete/<int:todo_id>', methods=['PUT'])
def complete(todo_id):

    """
    toggles the completed status of a task
    """

    todo = Todo.query.filter_by(id=todo_id).first_or_404()
    todo.complete()
    db.session.add(todo)
    db.session.commit()

    return todo_schema.jsonify(todo), 201

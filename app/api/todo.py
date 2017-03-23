#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from models import Task

app = Flask(__name__)


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.my_filter(task_id=task_id)
    if task:
        return jsonify(task)
    abort(404)


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(404)
    task = Task.create_task(request.json)
    return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def edit_task(task_id):
    task = Task.my_filter(task_id=task_id)
    if not Task.choke_input(task, req=request.json):
        abort(404)
    Task.update(task=task, req=request.json)
    return jsonify({'task': task})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.my_filter(task_id=task_id)
    if task:
        Task.delete(task)
        return jsonify({'results': True})
    else:
        abort(404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}))


@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'error': 'Access denied'}))


if __name__ == "__main__":
    app.run(debug=True)

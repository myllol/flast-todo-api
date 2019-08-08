from flask_restplus import Namespace, fields


class TodoDto:
    api = Namespace('todo', description='todo related operations')
    todo = api.model('todo', {
        'todo': fields.String(required=True, description='todo'),
    })
from app.main import db
from app.main.model.todo import Todo


def insert_todo(data):
    new_todo = Todo(
        todo=data['todo']
    )
    save_changes(new_todo)

    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201

def get_todos():
    return Todo.query.all()


def get_a_todo(id):
    return Todo.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
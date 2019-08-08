# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.todo_controller import api as todo_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='todolist',
          version='1.0',
          description='a todolist service'
          )

api.add_namespace(todo_ns, path='/todo')
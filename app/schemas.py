"""
Databse schemas for the api
"""
from .models import Todo
from . import ma

class TodoSchema(ma.ModelSchema):
    """
    Schemas for the todo model
    """
    class Meta:
        model = Todo

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

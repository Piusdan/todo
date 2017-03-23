"""
db modules
"""
from . import db  # import the db instance from app factory


class Todo(db.Model):
    """
    Todo class
    title: the title of the task
    completed: boolean that defines if the task is done
    """

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title):
        self.title = title

    def complete(self):
        """
        Returns true if task is complete and false otherwise
        """
        if self.completed:
            self.completed = False
        else:
            self.completed = True

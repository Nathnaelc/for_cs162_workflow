# tasks.py
from db import db


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    column = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'column': self.column
        }

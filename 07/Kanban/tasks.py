# tasks.py
from db import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    column = db.Column(db.String(50), nullable=False)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    history = db.relationship('History', backref='user', lazy=True)


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expression = db.Column(db.String(500), nullable=False)
    result = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

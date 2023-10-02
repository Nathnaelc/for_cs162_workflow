from flask import Flask, request, jsonify
from db import db
from tasks import Task
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configure SQLAlchemy settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app

db.init_app(app)


@app.route('/api/add_task', methods=['POST'])
def add_task():
    data = request.json
    task_description = data['description']
    # Default to 'toDo' if not provided
    task_column = data.get('column', 'toDo')
    new_task = Task(description=task_description, column=task_column)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'success': True})


@app.route('/api/get_tasks', methods=['GET'])
def get_tasks():
    tasks = {
        'toDo': [task.serialize() for task in Task.query.filter_by(column='toDo').all()],
        'inProgress': [task.serialize() for task in Task.query.filter_by(column='inProgress').all()],
        'inReview': [task.serialize() for task in Task.query.filter_by(column='inReview').all()],
        'done': [task.serialize() for task in Task.query.filter_by(column='done').all()],
    }
    return jsonify(tasks)


@app.route('/api/move_task/<task_id>/<column>', methods=['POST'])
def move_task(task_id, column):
    task = Task.query.get(task_id)
    if task:
        task.column = column
        db.session.commit()
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})


def create_tables():
    db.create_all()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

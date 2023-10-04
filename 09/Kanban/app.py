from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from db import db
from tasks import Task
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app, version='1.0', title='Kanban API',
          description='A simple Kanban API')

# Configure SQLAlchemy settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Model definition for Swagger documentation
task_model = api.model('Task', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'description': fields.String(required=True, description='Task description'),
    'column': fields.String(required=True, description='Task column')
})

# Task Resource


@api.route('/api/add_task')
class AddTaskResource(Resource):
    @api.expect(task_model)
    @api.marshal_with(task_model)
    def post(self):
        data = request.json
        task_description = data['description']
        task_column = data.get('column', 'toDo')
        new_task = Task(description=task_description, column=task_column)
        db.session.add(new_task)
        db.session.commit()
        return new_task


@api.route('/api/get_tasks')
class GetTasksResource(Resource):
    def get(self):
        tasks = {
            'toDo': [task.serialize() for task in Task.query.filter_by(column='toDo').all()],
            'inProgress': [task.serialize() for task in Task.query.filter_by(column='inProgress').all()],
            'inReview': [task.serialize() for task in Task.query.filter_by(column='inReview').all()],
            'done': [task.serialize() for task in Task.query.filter_by(column='done').all()],
        }
        return jsonify(tasks)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

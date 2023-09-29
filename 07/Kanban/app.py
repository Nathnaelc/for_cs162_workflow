# Import required modules from Flask and other files
from flask import Flask, render_template, request, redirect, url_for, jsonify
from db import db
from tasks import Task

# Initialize Flask app
app = Flask(__name__)

# Configure SQLAlchemy settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Route for the home page


@app.route('/')
def index():
    # Query tasks from the database and categorize them by their columns
    tasks = {
        'toDo': Task.query.filter_by(column='toDo').all(),
        'inProgress': Task.query.filter_by(column='inProgress').all(),
        'inReview': Task.query.filter_by(column='inReview').all(),
        'done': Task.query.filter_by(column='done').all()
    }
    # Render the HTML template and pass the tasks to it
    return render_template('session7.html', tasks=tasks)

# Route to add a new task, only allows POST method


@app.route('/add_task', methods=['POST'])
def add_task():
    # Get the task description from the form
    task_description = request.form.get('taskDescription')
    # Create a new Task object
    new_task = Task(description=task_description, column='toDo')
    # Add the new task to the database
    db.session.add(new_task)
    db.session.commit()
    # Redirect to the home page
    return redirect(url_for('index'))

# Route to move a task to a different column, only allows POST method


@app.route('/move_task/<task_id>/<column>', methods=['POST'])
def move_task(task_id, column):
    # Query the task by its ID
    task = Task.query.get(task_id)
    # Check if the task exists
    if task:
        # Update the column of the task
        task.column = column
        # Commit the changes to the database
        db.session.commit()
        # Return success status as JSON
        return jsonify({'success': True})
    else:
        # Return failure status as JSON if task doesn't exist
        return jsonify({'success': False})


# Main entry point of the app
if __name__ == '__main__':
    # Create all database tables
    with app.app_context():
        db.create_all()
    # Run the app in debug mode
    app.run(debug=True)

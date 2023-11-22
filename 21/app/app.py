# Import necessary modules from flask
from flask import Flask, render_template, request, redirect, url_for
# Import SQLAlchemy for database operations
from flask_sqlalchemy import SQLAlchemy
# Import Parser from parse module
from parse import Parser
# Import datetime module
from datetime import datetime

# Create a new Flask web server instance
app = Flask(__name__)

# Configure the SQLAlchemy instance with the SQLite database URI and disable track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy instance
db = SQLAlchemy(app)

# Define a new SQLAlchemy model called Expression


class Expression(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique id (primary key)
    text = db.Column(db.String(200))  # Expression text
    value = db.Column(db.Numeric)  # Calculated value of the expression
    # Timestamp of when the expression was evaluated
    now = db.Column(db.TIMESTAMP)


# Create all the necessary database tables
with app.app_context():
    db.create_all()

# Define the route for the index page


@app.route('/')
def index():
    # Query the database for the last 10 expressions, ordered by timestamp
    with app.app_context():
        exps = Expression.query.order_by(Expression.now.desc()).limit(10).all()
        # Render the index page with the queried expressions
        return render_template('index.html', expressions=exps)

# Define the route for adding a new expression, which accepts POST requests


@app.route('/add', methods=['POST'])
def add():
    # Get the expression from the form data
    expression = request.form['expression']
    # Parse and evaluate the expression
    p = Parser(expression)
    value = p.getValue()
    # Get the current time
    now = datetime.utcnow()

    # Add a new Expression to the database with the form data, calculated value, and current time
    with app.app_context():
        db.session.add(Expression(text=expression, value=value, now=now))
        db.session.commit()

    # Redirect to the index page
    return redirect(url_for('index'))


# Run the Flask web server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5162)

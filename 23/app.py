from flask import Flask, render_template, request, redirect, url_for, session
from auth import auth_blueprint
from calculator import evaluate_expression
from models import User, History, db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'today-is-a-long-day'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.register_blueprint(auth_blueprint)

db.init_app(app)

# function to create tables


def create_database(app):
    with app.app_context():
        db.create_all()


@app.route('/')
def index():
    user = None
    last_result = session.pop('last_result', None)

    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            history = History.query.filter_by(user_id=user.id).all()
            return render_template('dashboard.html', user=user, history=history, last_result=last_result)
        else:
            session.pop('user_id', None)  # Remove invalid user_id from session

    return redirect(url_for('auth.login'))


@app.route('/calculate', methods=['POST'])
def calculate():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    expression = request.form['expression']
    result = evaluate_expression(expression)
    user = User.query.get(session['user_id'])

    new_history = History(expression=expression,
                          result=result, user_id=user.id)
    db.session.add(new_history)
    db.session.commit()

    # Pass the result as a query parameter or store it in the session
    session['last_result'] = result
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.clear()  # This clears the entire session
    return redirect(url_for('auth.login'))  # Redirect to the login page


if __name__ == '__main__':
    create_database(app)
    app.run(debug=True)

## The Flask Microframework

Flask is called a microframework because it is lightweight and minimalistic,
providing the bare bones of features a simple web application requires. It
supports basic HTTP requests, connections to databases and a frontend, but
is easily extensible to a wide variety of other requirements.

Web/app frameworks have largely come to define modern app development, and you
will almost certainly run into them again at some point in the future. Try to
get a solid grasp of what frameworks accomplish, and why we have them! They
might seem complex and overwhelming at first, but they are the glue that makes
every part work with each other in a functioning application. They give us a
template/roadmap, or backbone if you will, to create dynamic and fun
applications in a much more efficient manner.

## Pre-class work

1. Work through thhe tutorial in question 1.
2. Answer all questions in Question 2, which will strengthen your knowledge with Flask.

### 1. Flask tutorial

Work through the official Flask tutorial:
https://flask.palletsprojects.com/en/2.3.x/tutorial/

This official Flask tutorial introduces the main features of Flask.
The focus today is on defining templates and views which are covered in the sections up
to the end of the _Blog Blueprint_ section. We cover topics like testing and deployment
later in the course.

- Work though the tutorial one section at a time.
- Use the internet and AI tools to help you debug if you get stuck.
- Research any code that you don't understand.
- **Commit the code to your PCW repo before you come to class**

### 2. Answer the following questions with as detail as possible

1. In your own words, what is Flask and why it is considered as a microframework?

Flask is a lightweight web framework written in Python. It's considered a microframework because it provides the essential tools to build a web application without including many of the additional features that larger frameworks might offer, such as form validation or database abstraction layers. This minimalistic approach gives developers the flexibility to add only what they need.

2. What are the roles of the following parts in a Flask app:

   - templates : These are files that contain the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.
   - static files: These are unchanging files like CSS, JavaScript, and images that are served as-is to the user.
   - requirements.txt: A file that lists all the Python dependencies required to run the Flask app.
   - virtual environment `venv`: An isolated environment where you can install Python packages without affecting the global Python installation.
   - render_template: A function in Flask used to render an HTML template and fill it with dynamic data.
   - redirect: A function to redirect the user to a different endpoint.
   - url_for: A function to generate URLs for given endpoints, ensuring that URLs remain consistent even if routes change.
   - session: A way to store information specific to a user from one request to the next.

3. When we run a Flask app, you may need to use the following commands. Explain the goal of each command.

   ```bash
   $ pip3 install -r requirements.txt
   ```

   -> Installs the Python packages listed in the requirements.txt file.

   ```bash
   $ export FLASK_APP=app
   ```

   -> Sets an environment variable indicating the entry point of the Flask application.

   ```bash
   $ python3 -m flask run
   ```

   -> Runs the Flask development server.

4. There are many ways to run a Flask model, the two common ways are

   ```bash
   export FLASK_APP=app.py
   python3 -m flask run
   ```

   -> sets the Flask application's entry point and then runs the Flask development server using the Flask module.
   or

   ```bash
   python3 app.py
   ```

   -> Using python3 app.py directly runs the app.py file as a Python script.

   Explain the differences between two commands, and when would you use each of them.

   The difference is in how the Flask environment is set up. The first method uses Flask's built-in development server, while the second relies on the script's execution. You'd typically use the first method during development for its built-in features like auto-reloading.

5. Why should we define specific version of libraries in `requirements.txt`? How can you find the version you should use?

Specifying versions ensures that the application behaves consistently across different environments from PC to PC. Without specific versions, it might inadvertently install newer packages with breaking changes. we can find the version you should use by checking the version we've tested with or by referring to the package's documentation.

6. What is the role of `@app.route` in the code below? Why do we put it right before defining the function. What is the default value for `methods` (in the documentation)?

   ```python
   @app.route('/', methods=['GET'])
   def main():
   	return 'Hello'
   ```

   @app.route is a decorator that tells Flask which URL should trigger the associated function. Placing it before a function binds that function to a URL endpoint. The default value for methods is ['GET']

7. What is a decorator? Why should we use decorators in our Flask app?
   A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. In Flask, decorators are used to route URLs to functions and to add functionalities like authentication.

8. What is the `config` attribute in a Flask app? How can you define `TESTING=True` or `SECRET_KEY='abc'`?
   This attribute in a Flask app is a dictionary-like object for storing configuration variables. I can set values like TESTING=True or SECRET_KEY='abc' using app.config['TESTING'] = True or app.config['SECRET_KEY'] = 'abc'.

9. Lots of modern servers normally return data in the JSON format. What is JSON and why should we use it?

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It's commonly used in modern web applications because of its simplicity and universality and swift speed.

10. What is the default host and port in Flask? How can you change the host and port?

The default host is 127.0.0.1 (localhost) and the default port is 5000.

Commit your answers to a README.md file in the repo. They don't have to be extensive written answers, just enough to prompt you into giving a complete verbal answer if you are called on.

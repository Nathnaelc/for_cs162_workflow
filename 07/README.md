## The Flask Microframework (part 2)

Todays class builds on the Flask tutorial from the previous session.
We look at 2 practices which help build larger Flask applications:

- Blueprints
- Flask packages

### Blueprints: Building with Structure

Blueprints serve as the cornerstone of structuring complex Flask
applications. In this session, we will focus on how they facilitate
modular design, enhance collaboration, and enable the development of
more substantial projects. By segmenting your applications into
distinct blueprints, each with its own routes and functionalities,
you'll be equipped to tackle projects of greater complexity and scope.

### Unveiling Flask Packages

Flask's ecosystem boasts a diverse array of packages that extend its
capabilities. You will work through a tutorial which uses:
`Flask-login` and `Flask-SQLAlchemy`. Pay attention to how these packages
are used to build a multi-user application.

## Pre-class work

### 1. Using Flask packages

Work through the following turorial on using Flask packages:
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

This app allows multiple users by making use of the Python packages Flask-login
and Flask-SQLAlchemy. After you have built this app, compare this app to the app
produced in the previous session. What is more complicated, and what is simpler?
Would any of the pros/cons change as the app grew in size?

### 2. Kanban board

In the session on HTML you were asked to design a Kanban board. Now that you
have learned about Flask, you can build a simple backend that persists data
to a database.

You can use the following simplifications to shorten the task:

1. There's no need to have users for this site. (As a result, no need for registration/login/logout)
2. All tasks can be created in the "To do" column.
3. The tasks can be moved to any column.

As always, you can use AI tools to help scaffold the necessary code.

Come to class with the server running on your laptop, able to give a short demo
if called on.

### 3. (Optional) Build a JSON API in Flask

It is best practice to separate out your application data from the presentation
of the data. Taken to its logical conclusion this leads to a clean separation
between static HTML and a JSON API. (Just like those APIs that were queried
in the previous session.)

Investigate the `jsonify()` method in Flask, as well as Flask `MethodViews`.
Together these can build a JSON API using sound object oriented principles.
As an example, one can use inheritance to ensure consistency between similar
end points.

One downside of this approach is that you now need to make client side requests.
Typically this is done in the webpage using JavaScript (or a JavaScript
framework). We will spend the next two sessions learning about React, which
is a JavaScript framework for building such webpages!

### 4. (Optional) Flask packages

Spend 10 minutes clicking around on the following site:
https://github.com/humiaozuzu/awesome-flask
Find an interesting Flask library and tell someone about it!

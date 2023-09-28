## React (part 1)

**Please note that
we are diving into an entirely new programming language (JavaScript) and
an entirely new framework (React). This is a lot to learn in one week,
so please start early, ask questions, search the internet, and use the
various AI tools to help (eg. Copilot and ChatGPT)**

After covering the basics of Flask (a backend framework), we now turn to
React (a frontend framework). React is a JavaScript library for building
user interfaces. It is maintained by Facebook, and is used in many
popular websites including Facebook, Instagram, and Netflix.

React is a popular choice for building user interfaces because it
provides a simple and intuitive way to build interactive webpages.
React is also popular because it is easy to learn, and because it
is easy to integrate with other JavaScript libraries.

## Pre-class work

### 1. Install Node.js

**Windows:**

If you are running Windows, then you will need to install Node.js using
Windows Subsystem for Linux (WSL). Follow the instructions here:
https://learn.microsoft.com/en-us/windows/wsl/install
And then follow this tutorial:
https://learn.microsoft.com/en-us/windows/dev-environment/javascript/react-on-wsl

**macOS:**

If you are running macOS, then you will need to install Node.js using
Homebrew. Follow the instructions here:
https://brew.sh/
and then run:

```bash
brew install node
```

**Linux:**
If you are running Linux, then you will need to install Node.js using
your package manager. For example, on Ubuntu you can run:

```bash
sudo apt install nodejs
```

### 2. React tutorial

This [React tutorial](https://blog.miguelgrinberg.com/post/the-react-mega-tutorial-chapter-1-modern-javascript) introduces
the React framework. Work through the first 5 chapters.

The

### 3. Kanban React app

In the previous sessions you designed a simple Kanban board, and
got to see some good designs from your classmates. Afterwards
we built a Flask app. Now it is time to revisit your design and
build a simple React app that implements it.

You can use the following simplifications to shorten the task:

- Just use static data. The data should be saved as a javascript variable,
  just like in the tutorial.
- There's no need to communicate with a server. (Even though we have
  a flask server which is almost ready to go!)
- There's no need to have users for this site. (As a result, no need
  for registration/login/logout)
- Put the form for entering a new task on a separate page. (This
  will be a gentle introduction to React routing.) In total your app
  should have 2 pages - the home page with some tasks in different
  stages, and the form for entering a new task. The form doesn't
  need to do anything at this stage!
- Each column of tasks should be the same reusable component.

### 4. Javascript questions

As you work through the React tutorial, you will undoubtably see
code that confuses you! This is normal. Please keep examples of
javascript that you found confusing, and bring them to class.
The examples should be in a format suitable for pasting into a
forum doc, and you should be able to clearly identify the
lines of code that you found confusing.

(It's even better if you initially found it confusing, but
now understand it! Bring those to class and help teach others!)

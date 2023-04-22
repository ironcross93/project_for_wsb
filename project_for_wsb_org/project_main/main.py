"""
Flask Application for greeting users with their name.

Author: Patryk Nowak
Date: 2023-03-04

Modules:
- Flask: a micro web framework for Python.
- render_template: a function in Flask used for rendering HTML templates.
- request: a module in Flask used for handling HTTP requests.

Endpoints:
- "/" endpoint displays a form where users can input their name.
- "/hello" endpoint greets the user with their name.
"""
from flask import Flask, render_template, request

main = Flask(__name__)


@main.route("/")
def hello():
    """
    Module: hello

    Description: This module contains the Flask route for the homepage ('/').
    When a user navigates to this route, they will see a form where they can
    enter their name. The form is defined in the 'hello.html' template.

    Routes:
        - '/': This route renders the 'hello.html' template.
    """
    return render_template("hello.html")


@main.route("/hello", methods=["GET", "POST"])
def greet():
    """
    Module : greet

    Flask view function that handles the form submission from the "hello.html" template.

    If the request method is POST, this function retrieves the value of the "name"
    input field from the submitted form data, and returns a greeting message with the
    provided name. Otherwise, it renders the "hello.html" template with an empty form.

    Returns:
        str or Flask response: If the request method is POST, returns a string with the
            greeting message. Otherwise, returns a Flask response object that renders
            the "hello.html" template with an empty form.

    Raises:
        KeyError: If the submitted form data does not contain a "name" field.
    """
    if request.method == "POST":
        name = request.form["name"]
        greeting = "Hello " + name
        return render_template("response.html", greeting=greeting)
    return render_template("hello.html")


if __name__ == "__main__":
    main.run(debug=True, host='0.0.0.0', port=8000)

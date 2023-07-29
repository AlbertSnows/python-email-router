import os

from flask import Flask, request, jsonify, render_template
from markupsafe import escape
# from werkzeug.datastructures import ImmutableMultiDict
from jsonschema import validate, exceptions, FormatChecker
import json

def act_on_file(path, func):
    with open(path, 'r') as file:
        return func(file)

def load_json_from_file(path):
    return act_on_file(path, json.load)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # todo: match with index
    @app.route("/")
    def entry():
        return "<p>Entry point!</p>"
      
    @app.route("/email", methods=["POST"])
    def process_email_routing_request():
      email_schema = load_json_from_file('./flaskr/schema/email.json')

      try:
        validate(request.json, email_schema, format_checker=FormatChecker())
        return request.json
      except exceptions.ValidationError as e:
        return jsonify(error=e.message)      
      
    @app.route("/hello")
    def hello():
        return "Hello, World!"
      
    @app.route("/write-any-text-after-slash/<text>")
    def anytext(text):
        return f"Text: {escape(text)}"

    # from . import db
    # db.init_app(app)

    # from . import auth
    # app.register_blueprint(auth.bp)

    # from . import blog
    # app.register_blueprint(blog.bp)
    # app.add_url_rule("/", endpoint="index")

    return app

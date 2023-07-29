import os

from flask import Flask, request, jsonify, render_template
from markupsafe import escape
from werkzeug.datastructures import ImmutableMultiDict
from jsonschema import validate, exceptions, FormatChecker
import json

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
      
      
    example_json = {
      "to": "fake@example.com",
      "to_name": "Mr. Fake",
      "from": "no-reply@fake.com",
      "from_name":"Ms. Fake",
      "subject": "A message from The Fake Family",
      "body": "<h1>Your Bill</h1><p>$10</p>"
    }
    
    schema = {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "title": "Email Request Handler",
      "description": "Schema to define expected json payload for email routing",
      "type": "object",
      "properties": {
        "to": {
          "description": "Email Receiver",
          "type": "string",
          "format": "email"},
        "to_name": {
          "description": "Receiver Name",
          "type": "string"},
        "from": {
          "description": "Sender Email",
          "type": "string",
          "format": "email"},
        "from_name": {
          "description": "Sender Name",
          "type": "string"},
        "subject": {
          "description": "Email Subject",
          "type": "string"},
        "body": {
          "description": "Email Description",
          "type": "string"}},
              "required": ["to", "to_name", "from", "from_name", "subject", "body"]}

    @app.route("/email", methods=["POST"])
    def process_email_routing_request():
      try:
        validate(request.json, schema, format_checker=FormatChecker())
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

import os

from flask import Flask, request, jsonify, render_template
from markupsafe import escape
from werkzeug.datastructures import ImmutableMultiDict
from jsonschema import validate, exceptions
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
          "type": "string"}}}

    @app.route("/email", methods=["POST"])
    def process_email_routing_request():
      content_type = request.headers.get("Content-Type")
      valid_json = content_type == "application/json" and request.json
      json = request.json if valid_json else "Either incorrect content type or not a post request"
      valid_json = validate(json) if valid_json else "Cannot validate payload"
      data_map = ImmutableMultiDict(json)
      
      try:
        validate(json.loads(example_json), schema)
        print("Validation successful. The data is valid against the schema.")
      except exceptions.ValidationError as e:
        print(f"Validation failed. Error: {e.message}")
      
      # form = email_request.EmailRequest(data_map) if valid_json else "Content-Type not supported!"
      return jsonify()
      populated_form = form #form.populate_obj(json)
      valid_form = valid_json and form.validate()
      valid_request = form.validate()
      if not valid_json:
        return form
      elif not valid_request:
        return request.json
      elif not valid_form:
        return jsonify(populated_form.errors)
      else:
        return jsonify(populated_form.data)

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

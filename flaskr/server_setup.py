import os

from flask import Flask, request, jsonify, render_template

def register_blueprints(app, blueprints):
    for bp in blueprints:
        app.register_blueprint(bp)
    return app

def initalize_app(test_config):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    return app

def initalize_instance_paths(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
      
def build_app(test_config):
		app = initalize_app(test_config)
		initalize_instance_paths(app)
		from flaskr.routes import entry
		from flaskr.routes import email
		app = register_blueprints(app, (entry.bp, email.bp))
		return app

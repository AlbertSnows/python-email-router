import os

from flask import Flask, request
from markupsafe import escape
from email_request import EmailRequest


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

    @app.route("/email", methods=['POST'])
    def process_email_routing_request():
      content_type = request.headers.get('Content-Type')
      valid_json = content_type == 'application/json' and request.POST
      form = EmailRequest(request.POST) if valid_json else 'Content-Type not supported!'
      valid_request = form.validate()
      if not valid_json:
        return form
      elif not valid_request:
        return request.json
      else:
        return "boop"
      
      
      if content_type == 'application/json':
        json = request.json
        form = EmailRequest(request.POST)
        return json;
      else:
        return 'Content-Type not supported!'

    @app.route("/hello")
    def hello():
        return "Hello, World!"
      
    @app.route("/write-any-text-after-slash/<text>")
    def anytext(text):
        return f'Text: {escape(text)}'

    # from . import db
    # db.init_app(app)

    # from . import auth
    # app.register_blueprint(auth.bp)

    # from . import blog
    # app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')

    return app

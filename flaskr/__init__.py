from flaskr.server_setup import build_app
# from werkzeug.datastructures import ImmutableMultiDict

def create_app(test_config=None):
    return build_app(test_config)
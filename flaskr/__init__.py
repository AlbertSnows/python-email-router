from flaskr.server_setup import build_app

def create_app(test_config=None):
    return build_app(test_config)
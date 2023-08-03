from flaskr.server_setup import build_app
from dotenv import load_dotenv

load_dotenv()

def create_app(test_config=None):        
    return build_app(test_config)
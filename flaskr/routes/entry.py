from flask import Blueprint, jsonify
bp = Blueprint("entry", __name__, url_prefix="/entry")
from markupsafe import escape

@bp.route("/")
def entry():
		return jsonify(message="Entry point!")
bp.add_url_rule("/", endpoint="index")

@bp.route("/hello")
def hello():
		return "Hello, World!"
	
@bp.route("/write-any-text-after-slash/<text>")
def anytext(text):
		return f"Text: {escape(text)}"

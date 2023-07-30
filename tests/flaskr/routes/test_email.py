import unittest

# from unittest.mock import match
from flaskr.routes.email import validate_input
from flaskr.utility.file import load_json_from_file

def test_validate_input():
    bad_json = {"foo": "bar"}
    bad_result = validate_input(bad_json)
    assert bad_result == {"error": "'to' is a required property"}

    good_json = load_json_from_file("./tests/flaskr/routes/data/good_email.json")
    good_result = validate_input(good_json)
    assert good_result == {"message": "Valid payload"}
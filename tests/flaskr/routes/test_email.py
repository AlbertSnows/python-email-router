import unittest
from unittest.mock import match
from flaskr.routes.email import validate_input
from flaskr.utility.file import load_json_from_file

def test_validate_input():
    bad_json = {"foo": "bar"}
    good_json = load_json_from_file('./data/good_email.json')
    bad_result = validate_input(bad_json)
    good_result = validate_input(good_json)
    print(bad_result)
    print(good_result)


# class TestMathOperations(unittest.TestCase):

#     def test_add(self):
#         # Original behavior
#         result = add(2, 3)
#         self.assertEqual(result, 5)

#         # Redefine the add function for testing purposes
#         with patch('math_operations.add', return_value=10):
#             # Now, the add function will always return 10 during this block
#             result = add(2, 3)
#             self.assertEqual(result, 10)

#         # The add function is back to its original behavior
#         result = add(2, 3)
#         self.assertEqual(result, 5)

# def test_index(client, auth):
#     response = client.get("/")
#     assert b"Log In" in response.data
#     assert b"Register" in response.data

#     auth.login()
#     response = client.get("/")
#     assert b"Log Out" in response.data
#     assert b"test title" in response.data
#     assert b"by test on 2018-01-01" in response.data
#     assert b"test\nbody" in response.data
#     assert b'href="/1/update"' in response.data

if __name__ == '__main__':
    unittest.main()
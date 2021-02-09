import unittest
from src.controller.controller import app
from flask import json
from src.util.constants.constants import *


class IntegratedTest(unittest.TestCase):

    def test__given__invalid_password__when__http_validate_password__then__return_http_code_ok(self):
        invalid_password_payload = {'password': 'invalidPass'}

        response = app.test_client().post(
            '/validate-password',
            data=json.dumps(invalid_password_payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(json.loads(response.get_data(as_text=True))['valid_password'])

    def test__given__valid_password__when__http_validate_password__then__return_http_code_ok(self):
        valid_password_payload = {'password': 'ValidP4$s'}

        response = app.test_client().post(
            '/validate-password',
            data=json.dumps(valid_password_payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.get_data(as_text=True))['valid_password'])

    def test__given__password_field_null__when__http_validate_password__then__return_http_code_bad_request(self):
        invalid_payload = {'password': None}

        response = app.test_client().post(
            '/validate-password',
            data=json.dumps(invalid_payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.get_data(as_text=True))['message'], PASSWORD_FIELD_NULL)

    def test__given__no_password_field__when__http_validate_password__then__return_http_code_bad_request(self):
        invalid_payload = {'no-password': 'ValidP4$s'}

        response = app.test_client().post(
            '/validate-password',
            data=json.dumps(invalid_payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.get_data(as_text=True))['message'], PASSWORD_FIELD_NOT_EXISTS)

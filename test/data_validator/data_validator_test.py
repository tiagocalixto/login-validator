import unittest
from werkzeug.exceptions import BadRequest
from src.controller.data_validator import DataValidator


class PasswordRuleValidatorDefaultUseCaseTest(unittest.TestCase):

    def test__given__payload_without_password_field__when__validate_payload__then__raise_bad_request(self):
        payload = {'no-password-field': 'test_1', 'no-password-field-two': 'test_2'}
        data_validator = DataValidator()
        self.assertRaises(BadRequest, data_validator.validate_password_payload, payload)

    def test__given__payload_with_null_password_field__when__validate_payload__then__raise_bad_request(self):
        payload = {'password': None}
        data_validator = DataValidator()
        self.assertRaises(BadRequest, data_validator.validate_password_payload, payload)


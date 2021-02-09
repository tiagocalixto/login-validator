import unittest
from unittest.mock import *
from src.use_case.validate_password_use_case import ValidatePasswordUseCase
from src.entity.password_payload import PasswordPayload
from src.entity.password_response import PasswordResponse


class ValidatePasswordUseCaseTest(unittest.TestCase):

    @patch('src.use_case.password_rule_default_use_case.PasswordRuleDefaultUseCase')
    def test__given__invalid_password_and_validator_default_class__when__validate_password__then__return_false(
            self, password_rule_mock):

        validate = ValidatePasswordUseCase(password_rule_mock)
        password_rule_mock.execute = Mock(return_value=PasswordResponse(False).to_dictionary())
        payload = PasswordPayload("invalid").to_dictionary()
        result = validate.execute(payload)
        self.assertFalse(result['valid_password'])
        password_rule_mock.execute.assert_any_call(payload)

    @patch('src.use_case.password_rule_default_use_case.PasswordRuleDefaultUseCase')
    def test__given__valid_password_and_validator_default_class__when__validate_password__then__return_true(
            self, password_rule_mock):

        validate = ValidatePasswordUseCase(password_rule_mock)
        password_rule_mock.execute = Mock(return_value=PasswordResponse(True).to_dictionary())
        payload = PasswordPayload("valid").to_dictionary()
        result = validate.execute(payload)
        self.assertTrue(result['valid_password'])
        password_rule_mock.execute.assert_any_call(payload)

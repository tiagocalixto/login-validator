import unittest
from src.factory.password_rule_factory import PasswordRuleFactory
from src.use_case.password_rule_default_use_case import PasswordRuleDefaultUseCase


class ValidatePasswordUseCaseTest(unittest.TestCase):

    def test__given__none_client__when__get_password_rule_class_by_client__then__return_default_rule_validator(self):
        result = PasswordRuleFactory().get_password_rule_class_by_client(None)
        self.assertEqual(type(result), type(PasswordRuleDefaultUseCase()))

    def test__given__any_client__when__get_password_rule_class_by_client__then__return_default_rule_validator(self):
        result = PasswordRuleFactory().get_password_rule_class_by_client('test_client')
        self.assertEqual(type(result), type(PasswordRuleDefaultUseCase()))

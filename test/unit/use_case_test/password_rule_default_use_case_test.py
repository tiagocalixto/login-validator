import unittest
from src.use_case.password_rule_default_use_case import PasswordRuleDefaultUseCase
from src.entity.password_payload import PasswordPayload


class PasswordRuleValidatorDefaultUseCaseTest(unittest.TestCase):

    def test__given__password_with_invalid_size__when__validate_password__then__return_false(self):
        password_eight_char_size = PasswordPayload('p@sSw0rd').to_dictionary()
        password_validator = PasswordRuleDefaultUseCase()
        result = password_validator.execute(password_eight_char_size)
        self.assertFalse(result['valid_password'])

    def test__given__password_without_numbers__when__validate_password__then__return_false(self):
        password_eight_char_size = PasswordPayload('p@sSword#').to_dictionary()
        password_validator = PasswordRuleDefaultUseCase()
        result = password_validator.execute(password_eight_char_size)
        self.assertFalse(result['valid_password'])

    def test__given__password_without_upper_case_char__when__validate_password__then__return_false(self):
        password_eight_char_size = PasswordPayload('p@s5word#').to_dictionary()
        password_validator = PasswordRuleDefaultUseCase()
        result = password_validator.execute(password_eight_char_size)
        self.assertFalse(result['valid_password'])

    def test__given__password_without_lower_case_char__when__validate_password__then__return_false(self):
        password_eight_char_size = PasswordPayload('P@S5WORD#').to_dictionary()
        password_validator = PasswordRuleDefaultUseCase()
        result = password_validator.execute(password_eight_char_size)
        self.assertFalse(result['valid_password'])

    def test__given__password_without_special_char__when__validate_password__then__return_false(self):
        password_eight_char_size = PasswordPayload('Pas5word1').to_dictionary()
        password_validator = PasswordRuleDefaultUseCase()
        result = password_validator.execute(password_eight_char_size)
        self.assertFalse(result['valid_password'])

    def test__given__password_with_blank_char__when__validate_password__then__return_false(self):
        password_eight_char_size = PasswordPayload('Pas5 word#').to_dictionary()
        password_validator = PasswordRuleDefaultUseCase()
        result = password_validator.execute(password_eight_char_size)
        self.assertFalse(result['valid_password'])

    def test__given__password_with_duplicated_char__when__validate_password__then__return_false(self):
        password_eight_char_size = PasswordPayload('P@ssW0rd#').to_dictionary()
        password_validator = PasswordRuleDefaultUseCase()
        result = password_validator.execute(password_eight_char_size)
        self.assertFalse(result['valid_password'])

    def test__given__valid_password__when__validate_password__then__return_true(self):
        password_eight_char_size = PasswordPayload('P@s5W0rd#').to_dictionary()
        password_validator = PasswordRuleDefaultUseCase()
        result = password_validator.execute(password_eight_char_size)
        self.assertTrue(result['valid_password'])

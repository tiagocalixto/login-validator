import logging
import re
from src.util.exception.password_exception import PasswordException
from src.util.constants.constants import *
from src.entity.password_response import PasswordResponse


class PasswordRuleDefaultUseCase(object):

    def __init__(self):
        self.password_payload = None

    def execute(self, password_payload):
        logging.info(VALIDATION_PASSWORD_DEFAULT)
        self.password_payload = password_payload

        try:
            self._format_password()
            self._validate_password_size()
            self._validate_password_contains_number_character()
            self._validate_password_contains_upper_case_character()
            self._validate_password_contains_lower_case_character()
            self._validate_password_contains_special_character()
            self._validate_password_not_contains_blank_character()
            self._validate_password_not_contains_duplicate_character()
            logging.info(VALIDATION_PASSWORD_DEFAULT_OK)
            return PasswordResponse(True).to_dictionary()
        except PasswordException as e:
            logging.error(e.message)
            return PasswordResponse(False).to_dictionary()

    def _format_password(self):
        logging.info(FORMAT_PASSWORD)
        self.password_payload['password'].strip()

    def _validate_password_size(self):
        logging.info(VALIDATING_PASSWORD_SIZE)

        if len(self.password_payload['password']) < 9:
            raise PasswordException(INVALID_PASSWORD_SIZE)

        logging.info(VALID_PASSWORD_SIZE)

    def _validate_password_contains_number_character(self):
        logging.info(VALIDATING_PASSWORD_NUMBER)

        if len(list(filter(lambda x: (x.isnumeric()),
                           self.password_payload['password']))) == 0:
            raise PasswordException(INVALID_PASSWORD_NO_NUMBER)

        logging.info(VALID_PASSWORD_NUMBER)

    def _validate_password_contains_upper_case_character(self):
        logging.info(VALIDATING_PASSWORD_UPPER)

        if len(list(filter(lambda x: (x.isupper()),
                           self.password_payload['password']))) == 0:
            raise PasswordException(INVALID_PASSWORD_NO_UPPER)

        logging.info(VALID_PASSWORD_UPPER)

    def _validate_password_contains_lower_case_character(self):
        logging.info(VALIDATING_PASSWORD_LOWER)

        if len(list(filter(lambda x: (x.islower()),
                           self.password_payload['password']))) == 0:
            raise PasswordException(INVALID_PASSWORD_NO_LOWER)

        logging.info(VALID_PASSWORD_LOWER)

    def _validate_password_contains_special_character(self):
        logging.info(VALIDATING_PASSWORD_SPECIAL_CHAR)

        pattern = re.compile('[!@#$%^&*()+-]')
        if pattern.search(self.password_payload['password']) is None:
            raise PasswordException(INVALID_PASSWORD_NO_SPECIAL_CHAR)

        logging.info(VALID_PASSWORD_SPECIAL_CHAR)

    def _validate_password_not_contains_blank_character(self):
        logging.info(VALIDATING_PASSWORD_BLANK_CHAR)

        if len(list(filter(lambda x: (x == ' '),
                           self.password_payload['password']))) > 0:
            raise PasswordException(INVALID_PASSWORD_CONTAINS_BLANK_CHAR)

        logging.info(VALID_PASSWORD_BLANK_CHAR)

    def _validate_password_not_contains_duplicate_character(self):
        logging.info(VALIDATING_PASSWORD_DUPLICATED_CHAR)

        password = self.password_payload['password']
        if len(set(password)) != len(list(password)):
            raise PasswordException(INVALID_PASSWORD_NO_DUPLICATED_CHAR)

        logging.info(VALID_PASSWORD_NOT_DUPLICATED_CHAR)

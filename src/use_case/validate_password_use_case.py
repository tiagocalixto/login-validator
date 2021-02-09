import logging
from src.util.constants.constants import *


class ValidatePasswordUseCase(object):

    def __init__(self, password_rule_validator):
        self.password_rule_validator = password_rule_validator

    def execute(self, password_payload):
        logging.info(VALIDATION_PASSWORD_USE_CASE_BEGIN + str(password_payload))
        response = self.password_rule_validator.execute(password_payload)
        logging.info(VALIDATION_PASSWORD_USE_CASE_END + str(response))
        return response

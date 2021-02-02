import logging
from src.util.constants.constants import *


class ValidatePasswordUseCase(object):

    def __init__(self, password_payload, password_rule_validator):
        self.password_payload = password_payload
        self.password_rule_validator = password_rule_validator

    def execute(self):
        logging.info(VALIDATION_PASSWORD_USE_CASE_BEGIN + str(self.password_payload))
        response = self.password_rule_validator.execute(self.password_payload)
        logging.info(VALIDATION_PASSWORD_USE_CASE_END + str(response))
        return response

import logging
from src.util.constants.constants import *
from src.use_case.password_rule_validator_default_use_case import PasswordRuleValidatorDefaultUseCase


class PasswordRuleFactory(object):

    @staticmethod
    def get_password_rule_class_by_client(client):
        """ como nao há nenhum client com regras específicas, por hora,
         apenas será retornado o validador default, conforme necessário,
         mais validadores podem ser incluídos """

        logging.info(FACTORY_PASSWORD_RULE_DEFAULT)
        return PasswordRuleValidatorDefaultUseCase()

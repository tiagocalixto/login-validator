from werkzeug.exceptions import BadRequest
from src.util.constants.constants import *
import logging


class DataValidator(object):

    @staticmethod
    def validate_password_payload(payload):

        if "password" not in payload:
            logging.error(PASSWORD_FIELD_NOT_EXISTS)
            raise BadRequest(PASSWORD_FIELD_NOT_EXISTS)

        if payload['password'] is None:
            logging.error(PASSWORD_FIELD_NULL)
            raise BadRequest(PASSWORD_FIELD_NULL)

        logging.info(PASSWORD_PAYLOAD_VALID)

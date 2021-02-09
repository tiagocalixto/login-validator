import logging
from datetime import date
from src.controller.data_validator import DataValidator
from flask import Flask
from flask import request
from flask import jsonify
from src.entity.password_payload import PasswordPayload
from src.use_case.validate_password_use_case import ValidatePasswordUseCase
from src.factory.password_rule_factory import PasswordRuleFactory
from src.util.constants.constants import *

app = Flask(__name__)


@app.route('/validate-password', methods=['POST'])
def validate_password():
    logging.info(START_PASSWORD_VALIDATOR_CONTROLLER)

    payload = request.get_json()
    logging.info('payload = ' + str(payload))

    DataValidator.validate_password_payload(payload)
    password = PasswordPayload.from_dictionary(payload)

    client = request.headers.get('client')
    logging.info('client = ' + str(client))

    password_rule_use_case = PasswordRuleFactory.get_password_rule_class_by_client(client)
    password_validator_use_case = ValidatePasswordUseCase(password_rule_use_case)
    response = password_validator_use_case.execute(password.to_dictionary())
    logging.info('response = ' + str(response))

    logging.info(END_PASSWORD_VALIDATOR_CONTROLLER)
    return jsonify(response), 200


@app.errorhandler(400)
def bad_request_handler(e):
    message = str(e).split("400 Bad Request: ", 1)[1]
    error_dict = format_error_message(BAD_REQUEST, 400, message)
    logging.error(error_dict)
    return jsonify(error_dict), 400


@app.errorhandler(405)
def method_not_allowed_handler(e):
    message = str(e).split("405 Method Not Allowed: ", 1)[1]
    error_dict = format_error_message(METHOD_NOT_ALLOWED, 405, message)
    logging.error(error_dict)
    return jsonify(error_dict), 405


@app.errorhandler(500)
def internal_server_error_handler(e):
    error_dict = format_error_message(INTERNAL_SERVER_ERROR, 500, INTERNAL_SERVER_ERROR_MESSAGE)
    logging.error(error_dict)
    return jsonify(error_dict), 500


def format_error_message(status, code, message):
    return {'date': date.today(),
            'status': status,
            'status_code': code,
            'message': message
            }


if __name__ == '__main__':
    app.run(debug=True)

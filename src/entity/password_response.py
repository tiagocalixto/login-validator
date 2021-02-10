class PasswordResponse(object):

    def __init__(self, valid_password):
        self.valid_password = valid_password

    @staticmethod
    def from_dictionary(dictionary):
        return PasswordResponse(
            valid_password=dictionary['valid_password']
        )

    def to_dictionary(self):
        return {
            'valid_password': self.valid_password
        }

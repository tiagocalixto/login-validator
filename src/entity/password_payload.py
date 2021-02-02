class PasswordPayload(object):

    def __init__(self, password):
        self.password = password

    @staticmethod
    def from_dictionary(dictionary):
        return PasswordPayload(
            password=dictionary['password']
        )

    def to_dictionary(self):
        return {
            'password': self.password
        }

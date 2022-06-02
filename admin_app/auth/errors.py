
class UserExistsException(Exception):
    error_code = 1051

    def __repr__(self):
        return "This User Name has already been registered"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class UserEmailExistsException(Exception):
    error_code = 105

    def __repr__(self):
        return "This email address has already been registered"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class UserNotFoundException(Exception):
    error_code = 107

    def __repr__(self):
        return "User not found"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class WrongPasswordException(Exception):
    error_code = 108

    def __repr__(self):
        return "Wrong password"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class WrongEmailException(Exception):
    error_code = 109

    def __repr__(self):
        return "Wrong email"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class IncorrectEmailException(Exception):
    error_code = 110

    def __repr__(self):
        return "Incorrect email"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class ValidHeaderTokenMissingException(Exception):
    error_code = 121

    def __repr__(self):
        return "A valid header for token is missing"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class TokenIsInvalidException(Exception):
    error_code = 122

    def __repr__(self):
        return "Token is invalid"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class UserLoginRequiredException(Exception):
    error_code = 123

    def __repr__(self):
        return "User login required"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class FriendExistsException(Exception):
    error_code = 131

    def __repr__(self):
        return "Exists entry"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class FriendStatusIsNotRequestedException(Exception):
    error_code = 132

    def __repr__(self):
        return "Friend status is not requested"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class FriendStatusIsNotApprovedException(Exception):
    error_code = 133

    def __repr__(self):
        return "Friend status is not approved"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]


class CannotUnblockFriendException(Exception):
    error_code = 134

    def __repr__(self):
        return "You have been blocked by this user. Wait for the user to unblock you"

    def __format__(self, format_spec=None):
        return [{'error_code': self.error_code, 'error_message': self.__repr__()}]

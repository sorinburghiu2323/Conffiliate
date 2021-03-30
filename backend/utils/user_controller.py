import re

from rest_framework.exceptions import ValidationError


def validate_password(password):
    """
    Validate user password.
    :param password: password as string.
    :return: True - valid password.
             Any string - invalid password.
    """
    flag = ""
    if len(password) < 8:
        flag += "\n At least 8 characters"
    if not re.search("[a-z]", password):
        flag += "\n At least 1 lower case character"
    if not re.search("[A-Z]", password):
        flag += "\n At least 1 upper case character"
    if not re.search("[0-9]", password):
        flag += "\n At least 1 number"
    if re.search("\s", password):
        flag += "\n No spaces"
    if flag:
        raise ValidationError("Password must contain: " + flag)
    return True

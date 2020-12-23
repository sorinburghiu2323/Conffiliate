import re

from affiliate_mvp.models import Platform, User


def validate_user_data(name, email, phone):
    """
    Check if influencer data is adequate.
    :param name: string - user's name
    :param email: string - user's email
    :param phone: string - user's phone number
    :return: False - data is valid
    """
    if name.isspace() or name == "" or len(name) > 64:
        return "Name cannot be empty or too large."
    if "@" not in email:
        return "Email cannot be empty and must be valid."
    if User.objects.filter(email=email).exists():
        return "Email is already in use."
    if phone.isspace() or phone == "" or len(phone) > 64:
        return "Phone number cannot be empty or too large."
    return False


def validate_keywords(keywords):
    """
    Check if keywords are in the right format.
    :param keywords: string of keywords
    :return: False - keywords are in the right format
    """
    try:
        re.sub("[^\w]", " ", keywords).split()
        return False
    except:
        return "Keywords were not in the adequate format."


def validate_platform(platform):
    """
    Check if platform exists.
    :param platform: string name of the platform
    :return: False - platform exists
    """
    if not Platform.objects.filter(name=platform).exists():
        return "Platform does not exist."
    return False


def validate_password(password, password_repeat=None):
    """
    Validate user password.
    :param password: password as string
    :param password_repeat: repeat password
    :return: False - valid password
    """
    if password_repeat:
        if password != password_repeat:
            return "Passwords did not match."
    flag = False
    if len(password) < 8:
        flag = True
    elif not re.search("[a-z]", password):
        flag = True
    elif not re.search("[A-Z]", password):
        flag = True
    elif not re.search("[0-9]", password):
        flag = True
    elif not re.search("[$&+,:;=?@#|'<>.^*()%!-]", password):
        flag = True
    elif re.search("\s", password):
        flag = True
    if flag:
        return "Password must contain at least a lower case, an upper case, a number, a symbol (e.g. !$%) " \
               "and not spaces."
    return False

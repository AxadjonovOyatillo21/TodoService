from src.validators_tools.common_validators import length_validator


def password_validator(value):
    if not length_validator(value):
        return False
    if not (isinstance(value, str) and value.isalnum() and len(value) > 6):
        return False
    return True



def is_true(value):
    return True if value else False


def email_validator(value):
    if not value:
        return False
    if not ("@" in value):
        return False
    parts = value.split("@")
    if not (parts[0].isalnum() and len(parts[-1]) > 5):
        return False
    if not("." in parts[-1]):
        return False
    parts_1 = parts[-1].split(".")
    if not (len(parts_1[-1]) >= 2):
        return False
    if not (len(parts_1[0]) >= 4):
        return False
    return True


# updated with early exit strategy

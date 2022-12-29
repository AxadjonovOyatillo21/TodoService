from src.validators_tools.common_validators import length_validator


def password_validator(value):
    if length_validator(value):
        if isinstance(value, str) and value.isalnum() and len(value) > 6:
            return True
        else:
            return False
    else:
        return False


def is_true(value):
    return True if value else False


def email_validator(value):
    if value:
        if "@" in value:
            parts = value.split("@")
            if parts[0].isalnum() and len(parts[-1]) > 5:
                if "." in parts[-1]:
                    parts_1 = parts[-1].split(".")
                    if len(parts_1[-1]) >= 2:
                        if len(parts_1[0]) >= 4:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

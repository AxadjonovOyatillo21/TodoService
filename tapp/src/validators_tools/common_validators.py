data_rules = {
    "deadline_rules": [
        "The deadline should be in the following format: D-day, M-Month, Y-year: ",
        "Each part, such as day, month, and year should be equal to the time in now or higher than now",
        "Each part should be an integer",
        "That's all :D"
    ],
    "username_rules": [
        "The username should be a string!",
        "The username should include letters and numbers, but shouldn't include empty spaces!",
        "The username must be unique!",
        "That's all :)"
    ],
    "email_rules": [
        "Email should include @ symbol and next to it should be the address of the service like ...@gmail.com!",
        "Email should be unique!",
        "That's all (0-0)"
    ]
}


def length_validator(value):
    if value:
        value_splitted = value.split()
        if len(value_splitted) >= 1:
            if value and len(value) > 3:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

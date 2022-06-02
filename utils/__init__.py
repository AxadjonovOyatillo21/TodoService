from datetime import datetime


TODO_OR_TODOLIST_PER_PAGE = 5
now = datetime.utcnow


class Pagination:
    def paginate_item(self, request, selection):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * TODO_OR_TODOLIST_PER_PAGE
        end = start + TODO_OR_TODOLIST_PER_PAGE
        items = [item.format() for item in selection]
        current_items = items[start:end]
        return current_items


def length_validator(value):
    value_splitted = value.split()
    if len(value_splitted) >= 1:
        if value and len(value) > 3:
            return True
        else:
            return False
    else:
        return False


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


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


months_info = {
    "January": {
        "days": 31
    },
    "February": {
        "days": 29
    },
    "March": {
        "days": 31
    },
    "April": {
        "days": 30
    },
    "May": {
        "days": 31
    },
    "June": {
        "days": 30
    },
    "July": {
        "days": 31
    },
    "August": {
        "days": 31
    },
    "September": {
        "days": 30
    },
    "October": {
        "days": 31
    },
    "November": {
        "days": 30
    },
    "December": {
        "days": 31
    }
}


numbers = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "nineth",
    "tenth",
    "eleventh",
    "twelvth"
]


def deadline_validator(deadline):
    if deadline:
        if "/" in deadline:
            if isinstance(deadline, str):
                parts = [part for part in deadline.split("/") if part]
                for part in parts:
                    if not part.isdigit():
                        return {
                            "message": "Please enter correct deadline, each part should be integer like 02, 22, 21!",
                            "success": False
                        }
                if len(parts) == 3:
                    day = int(parts[0])
                    month = int(parts[1])
                    year = int(parts[-1])
                    if year >= now().year:
                        if month <= 12:
                            if year == now().year:
                                if month >= now().month:
                                    if day <= months_info[months[month - 1]]["days"]:
                                        if day >= now().day:
                                            return {
                                                "message": f"Woohoo! All data are correct!",
                                                "deadline": f"{'0' + str(day) if day < 10 else day}/{'0' + str(month) if month < 10 else month}/{'0' + str(year) if year < 10 else year}",
                                                "success": True
                                            }
                                        else:
                                            return {
                                                "message": f"You are entered day {day}, year {year}, month {months[month - 1]}, but now is {now().day}-day of {months[now().month - 1]} of {now().year} year!",
                                                "success": False
                                            }
                                    else:
                                        return {
                                            "message": f"Have you ever seen day {day}, we have only {months_info[months[month - 1]]['days']} days in {months[month - 1]}! OK?",
                                            "success": False
                                        }
                                else:
                                    return {
                                        "message": f"You are entered month {months[month - 1]}, but now is {numbers[now().month - 1]} month: {months[now().month - 1]}",
                                        "success": False
                                    }
                            else:
                                if day <= months_info[months[month - 1]]["days"]:
                                    return {
                                        "message": f"Woohoo! All data are correct!",
                                        "deadline": f"{'0' + str(day) if day < 10 else day}/{'0' + str(month) if month < 10 else month}/{'0' + str(year) if year < 10 else year}",
                                        "success": True
                                    }
                                else:
                                    return {
                                        "message": f"Have you ever seen day {day}, we have only {months_info[months[month - 1]]['days']} days in {months[month - 1]}! OK?",
                                        "success": False
                                    }                        
                        else:
                            return {
                                "message": f"Have you ever seen month {month}, we only have 12 monthes! OK?",
                                "success": False
                            }
                    else:
                        return {
                            "message": f"You are entered year {year} :D Time travelling isn\'t possible for now) \
                            But according to theory of relativity we can travel to \"Future\" :D So for now, enter year equal to or higher than year in now, OK? Now is {now().year})",
                            "success": False
                        }
                else:
                    return {
                        "message": "Hey, deadline should include three parts: day, month, year. Try again :D",
                        "success": False
                    }
            else:
                return {
                    "message": "Please enter correct deadline, following in this format: DD/MM/YYYY",
                    "success": False
                }
        else:
            return {
                "message": "Please enter correct deadline, following in this format: DD/MM/YYYY",
                "success": False
            }

    else:
        return {
            "message": "Please enter correct deadline, in fllowing format: DD/MM/YYYY",
            "success": False
        }


data_rules = {
    "deadline_rules": [
        "Deadline should be in following format: D-day, M-Month, Y-year: DD/MM/YY",
        "Each part, such as day, month and year should be equal to time in now or higher than now",
        "Each part should be integer",
        "That's all :D"
    ],
    "username_rules": [
        "Username should be string!",
        "Username should include letters and number, but shouldn't include empty spaces!",
        "Username must be unique!",
        "That's all :)"
    ],
    "email_rules": [
        "Email should include @ symbol and next of it should be address of service like ...@gmail.com!",
        "Email should be unique!",
        "That's all (0-0)"
    ]
}

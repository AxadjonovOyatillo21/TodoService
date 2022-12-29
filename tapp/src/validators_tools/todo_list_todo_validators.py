import calendar
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


# months_info = {
#     "January": {
#         "days": 31
#     },
#     "February": {
#         "days": 29
#     },
#     "March": {
#         "days": 31
#     },
#     "April": {
#         "days": 30
#     },
#     "May": {
#         "days": 31
#     },
#     "June": {
#         "days": 30
#     },
#     "July": {
#         "days": 31
#     },
#     "August": {
#         "days": 31
#     },
#     "September": {
#         "days": 30
#     },
#     "October": {
#         "days": 31
#     },
#     "November": {
#         "days": 30
#     },
#     "December": {
#         "days": 31
#     }
# }


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
                            "message": "Please enter correct deadline, "
                            "each part should be integer like 02, 22, 21!",
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
                                    if day <= calendar.monthrange(now().year, month)[1]:
                                        if day >= now().day:
                                            return {
                                                "message": f"Woohoo! All data are correct!",
                                                "deadline": f"{'0' + str(day) if day < 10 else day}"
                                                f"/{'0' + str(month) if month < 10 else month}"
                                                f"/{'0' + str(year) if year < 10 else year}",
                                                "success": True
                                            }
                                        else:
                                            return {
                                                "message": f"You are entered day {day}, year {year}, "
                                                f"month {months[month - 1]}, but now is {now().day}-day "
                                                f"of {months[now().month - 1]} of {now().year} year!",
                                                "success": False
                                            }
                                    else:
                                        return {
                                            "message": f"Have you ever seen day {day}, "
                                            f"we have only {calendar.monthrange(now().year, month)[1]}"
                                            f"days in {months[month - 1]} in this year! OK?",
                                            "success": False
                                        }
                                else:
                                    return {
                                        "message": f"You are entered month {months[month - 1]}, "
                                        f"but now is {numbers[now().month - 1]} month: {months[now().month - 1]}",
                                        "success": False
                                    }
                            else:
                                if day <= calendar.monthrange(now().year, month)[1]:
                                    return {
                                        "message": f"Woohoo! All data are correct!",
                                        "deadline": f"{'0' + str(day) if day < 10 else day}"
                                        f"/{'0' + str(month) if month < 10 else month}"
                                        f"/{'0' + str(year) if year < 10 else year}",
                                        "success": True
                                    }
                                else:
                                    return {
                                        "message": f"Have you ever seen day {day}, "
                                        f"we have only {calendar.monthrange(now().year, month)[1]} days in {months[month - 1]}! OK?",
                                        "success": False
                                    }
                        else:
                            return {
                                "message": f"Have you ever seen month {month}, we only have 12 monthes! OK?",
                                "success": False
                            }
                    else:
                        return {
                            "message": f"You are entered year {year} :D Time travelling isn\'t possible for now)"
                            "But according to theory of relativity we can travel to \"Future\""
                            f":D So for now, enter year equal to or higher than year in now, OK? Now is {now().year})",
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

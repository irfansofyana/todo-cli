import datetime


def validate_time(val):
    try:
        datetime.datetime.strptime(val, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_importance(val):
    val = int(val)
    return val >= 1 and val <= 10


def validate_urgency(val):
    val = int(val)
    return val >= 1 and val <= 10

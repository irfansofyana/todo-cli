import datetime


def validate_time(val):
    try:
        datetime.datetime.strptime(val, "%Y-%m-%d")
        return True
    except ValueError:
        return False

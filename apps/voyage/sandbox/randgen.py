import datetime
import random

from .sampledata import firstnames, lastnames


def random_userdata():
    fname = random_firstname()
    lname = random_lastname()
    email = f"{fname.lower()[0]}{lname.lower()}@random.enineschool.com"
    result = {
        "username": email,
        "first_name": fname,
        "last_name": lname,
        "email": email,
    }

    print(result)
    return result


def random_firstname():
    return random.choice(firstnames)


def random_lastname():
    return random.choice(lastnames)


def random_phonenumber():
    result = str(random.randint(6, 9))
    result += "".join([str(random.randint(0, 9)) for _ in range(9)])
    return result


def random_date(years=None):
    """
    Returns a random date between date range provided if provided or
    in the last 50 years ago ending today.
    """
    if years is None:
        current_year = datetime.date.today().year
        years = range(current_year - 49, current_year + 1)

    year = random.randint(years[0], years[-1])
    number_of_days = datetime.date(year + 1, 1, 1) - datetime.date(year, 1, 1)
    dates = [
        datetime.date(year, 1, 1) + datetime.timedelta(days=x)
        for x in range(0, number_of_days.days)
    ]
    return random.choice(dates)

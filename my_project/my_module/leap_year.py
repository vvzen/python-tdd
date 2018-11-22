def check_leap_year(year):

    if isinstance(year, str):
        raise AssertionError('String was given as input')

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
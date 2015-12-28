"""
Code by Gonzalo Rolon Morinelli, Dec 27 2015.

The following code was originally written as a solution for Project Euler's
Problem# 19
For more information, goto: https://projecteuler.net/problem=19
"""


from math import floor


DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday']


def compute_day_of_week(year, month, d):
    """Return the day of the week for the date year/month/d.

    Custom implementation of Gauss algorithm to determine the day of the week.
    """
    m = (month - 2) % 12
    c = int(str(year)[:2])
    y = int(str(year)[2:])
    if month < 3:
        y -= 1
    m = floor(2.6 * m - 0.2)
    y = (y + floor(y / 4))
    c = (floor(c / 4) - 2 * c)
    day = (d + m + y + c)
    day = int(day) % 7
    return DAYS[day]


def compute_count_day(day, i_year, e_year, t_date):
    """Return the count of days where t_date falls on a given day."""
    t_ctr = 0
    for year in range(i_year, e_year + 1):
        for month in range(1, 13):
            if compute_day_of_week(year, month, t_date) == day:
                t_ctr += 1
    return t_ctr

if __name__ == '__main__':
    # Problem solution.
    print compute_count_day('Sunday', 1901, 2000, 1)

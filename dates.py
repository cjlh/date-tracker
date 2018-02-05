#!/usr/bin/env python3

"""A Python script for keeping track of important dates.

File name: dates.py
Author: Caleb Hamilton
Date created: 2018-02-05
Date last modified: 2018-02-05
License: GNU GPLv3
Python Version: 3

Usage:
    $ python dates.py

"""

import datetime


terminal_colors = {
    'blue': '\033[34m',
    'normal': '\033[0m',
    'grey': '\033[37m',
    'white': '\033[97m',
    'green': '\033[32m',
    'cyan': '\033[36m',
    'yellow': '\033[33m',
    'light_yellow': '\033[93m',
    'light_blue': '\033[93m',
    'light_red': '\033[91m'
}


def time_until(y, m, d):
    return str((datetime.date(y, m, d) - datetime.date.today()).days)


def day_of_date(y, m, d):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    return days[datetime.datetime(y, m, d).weekday()]


def print_assignment_details(title, date, color):
    print(terminal_colors[color] + title + ': ' +
          terminal_colors['white'] + time_until(date[0], date[1], date[2]) +
          terminal_colors['normal'] + ' days (' +
          day_of_date(date[0], date[1], date[2]) + ')')


assignments = [
    ('Digital Communication', (2018, 2, 16), 'blue'),
    ('Software Engineering', (2018, 2, 23), 'yellow'),
    ('Group Project (LSEPI)', (2018, 3, 2), 'yellow'),
    ('Networks and Systems', (2018, 3, 9), 'normal'),
    ('Computer Graphics', (2018, 3, 16), 'blue'),
    ('Theory of Computation benchtest', (2018, 3, 12), 'light_red'),
    ('Systems Programming bechtest', (2018, 3, 13), 'green')
]

for assignment in assignments:
    print_assignment_details(assignment[0], assignment[1], assignment[2])

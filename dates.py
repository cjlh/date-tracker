#!/usr/bin/env python3

""" A Python script for keeping track of important dates.

File name: dates.py
Author: Caleb Hamilton
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
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
    return days[datetime.datetime(y, m, d).weekday()]


def print_event_details(title, date, color):
    print(terminal_colors[color] + title + ': ' +
          terminal_colors['white'] + time_until(date[0], date[1], date[2]) +
          terminal_colors['normal'] + ' days (' +
          day_of_date(date[0], date[1], date[2]) + ')')


def main():
    events = [
        ('Example event', (2345, 6, 7), 'blue'),
    ]

    for event in events:
        print_event_details(event[0], event[1], event[2])


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

""" A Python script for keeping track of important dates.

File name: dates.py
Author: Caleb Hamilton
Website: https://github.com/cjlh/date-tracker
License: GNU GPLv3
Python version: 3

Usage:
    $ python dates.py
"""

import datetime
import yaml
import sys


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


def load_events(filepath):
    """ Loads dates from the given yaml filepath.

    Args:
        filepath (str): The file from which to load the configuration.

    TODO:
        - check given date is valid
        - check given color is valid
        - add check for '.yml'
    """
    with open(filepath, 'r') as events_file:
        try:
            events_dict = yaml.safe_load(events_file)
        except yaml.YAMLError as yaml_e:
            raise ValueError('Error in \'events.yaml\' file')
    events_list = []
    for event in events_dict['events']:
        events_list.append((event['name'], event['date'], event['color']))
    return events_list


def time_until(date_string):
    """ Returns the number of days until a given date.

    Args:
        date_str (str): A date given in ISO 8601 format.
    """
    try:
        # Parse date date object from given string
        given_date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError:
        print('Error: given date is not in the required format')
        exit()
    date_today = datetime.date.today()
    return str((given_date - date_today).days)


def day_of_date(date_string):
    """ Returns the day of the week of a given date.

    Args:
        date_string (str): A date given in ISO 8601 format.
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
    try:
        given_date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError:
        print('Error: given date is not in the required format')
        exit()
    return days[given_date.weekday()]


def print_event_details(name, date_string, color):
    """ Prints out the details of a given event.

    Args:
        name (str): The name of the event.
        date_string (str): The date of the event.
        color (str): The color with which to print out the event's name (this
            must be a valid key in the `terminal_colors` dictionary.
    """
    print(terminal_colors[color] + name + ': ' +
          terminal_colors['white'] + time_until(date_string) +
          terminal_colors['normal'] + ' days (' +
          day_of_date(date_string) + ')')


def help():
    """ Prints out instructions on how to use this script.
    """
    print('TODO')


def main():
    """ The main program function.
    """
    try:
        events = load_events('events.yaml')
    except OSError:
        print('Error: config file does not exist. For instructions on how to use dates.py, please use the \'-h\' flag (\'python dates.py -h\')')
        exit()
    except ValueError:
        print('Error: invalid config file format. For instructions on how to use dates.py, please use the \'h\' flag (\'python dates.py -h\')')
        exit()
    # Loop through events and print the details of each
    for event in events:
        print_event_details(event[0], event[1], event[2])


if __name__ == '__main__':
    if (len(sys.argv) == 2 and sys.argv[1] == '-h'):
        help()
    else:
        main()

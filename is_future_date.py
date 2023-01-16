"""This is the python module used to check whether the given date is future date.

This module takes below parameters.
date -- The date to check. Provide the date in format yyyy-MM-dd. e.g. 2023-01-16
"""

import datetime
import argparse

parser = argparse.ArgumentParser(
    description='Checks the given date with current date and returns true if it is future date'
)
parser.add_argument(
    '-d',
    '--date',
    required=True,
    help='Provide the date to check (in format yyyy-MM-dd) e.g. 2023-01-16')

args = parser.parse_args()
input_date = args.date

def is_future(input_date):
    """Checks whether the given date is future date

    Args:
        input_date (str): date to check (in format yyyy-MM-dd) e.g. 2023-01-16

    Returns:
        bool: whether it is future date
    """
    # Cast specific date to Date Python Object
    date = datetime.datetime.strptime(input_date, '%Y-%m-%d').date()
    # Get today date with Date Python Object
    today = datetime.date.today()
    return date > today

print (is_future(input_date))

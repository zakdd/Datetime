# https://codechalleng.es/bites/67/ coding challenge 
from datetime import date, timedelta

start_100days = date(2020, 7, 9)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    final_days = start_100days + timedelta(days=100)
    print(final_days)
    #pass


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    diff = abs(pycon_date - pybites_founded)
    print(diff)
    #pass


get_hundred_days_end_date()
get_days_between_pb_start_first_joint_pycon()

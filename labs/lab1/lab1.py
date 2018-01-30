"""
Jon Shallow
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    """
    This function returns a string value
    """
    return "Hello, world!"

def give_me_an_integer():
    """
    This function returns an integer value
    """
    return 5

def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    return True

def give_me_a_float():
    """
    This function returns a float value
    """
    return 3.2

def give_me_a_list():
    """
    This function returns a list
    """
    return [1,2,3]

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    return {'Team': 'USA', 'Gold Medals': '36', 'Silver Medals': '24', 'Bronze Medals': '32'}

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    return ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    sum = 0
    for number in range(1, 11):
        sum = sum + number 
    return sum

def check_is_even(number):
    """
    This function returns True if num is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    if (number % 2 == 0):
        return True
    else:
        return False

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """
    if (number1 < number2):
        return True
    else:
        return False

#! /usr/bin/python

"""
This script generates a random EAN13 number and prints it to the standard out.
"""

from random import randrange

# importing functools for reduce()
import functools

def generate_12_random_numbers():
    numbers = []
    for x in range(12):
        numbers.append(randrange(10))
    return numbers

def calculate_checksum(ean):
    """
    Calculates the checksum for an EAN13
    @param list ean: List of 12 numbers for first part of EAN13
    :returns: The checksum for `ean`.
    :rtype: Integer
    """
    assert len(ean) == 12, "EAN must be a list of 12 numbers"
    sum_ = lambda x, y: int(x) + int(y)
    evensum = functools.reduce(sum_, ean[::2])
    oddsum = functools.reduce(sum_, ean[1::2])
    return (10 - ((evensum + oddsum * 3) % 10)) % 10

numbers = generate_12_random_numbers()
numbers.append(calculate_checksum(numbers))
print (''.join(map(str, numbers)))


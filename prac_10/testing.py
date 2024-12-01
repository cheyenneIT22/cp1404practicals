"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


#
def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a full stop.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('this is a test')
    'This is a test.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase.capitalize()


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    car = Car()
    assert car.odometer == 0, "Car does not set odometer correctly"

    default_car = Car()
    assert default_car.fuel == 0, "Car does not set fuel to default correctly"

    # Test fuel initialization with a specific value
    specific_car = Car(fuel=10)
    assert specific_car.fuel == 10, "Car does not set specific fuel correctly"
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
#   'hello' -> 'Hello.'
#   'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more that you decide is a useful test.
# Run your doctests and watch the tests fail.
# Then write the body of the function so that the tests pass.
# Test default fuel initialization

run_tests()

# Run doctests
doctest.testmod()

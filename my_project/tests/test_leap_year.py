import pytest
import my_module
from my_module.leap_year import check_leap_year

# EXAMPLES OF A TDD FUNCTION
# Write some code that given a year,
# returns True if it's a leap year and false otherwise
# A leap year is :
# divisible by 4
# not divisible 100
# if divisible by 100, it must be divisible by 400

def assertLeapYear(year, expected_result):
    assert check_leap_year(year) == expected_result

def test_isFalseIfDivisibleBy4():
    assertLeapYear(1995, False)

def test_isTrueIfDivisibleBy4():
    assertLeapYear(1996, True)

def test_isFalseIfDivisibleBy4And100AndNot400():
    assertLeapYear(2100, False)

def test_isTrueIfDivisibleBy4And100And400():
    assertLeapYear(1600, True)

# check if the function raises an exception
def test_isFalseIfGivenString():
    with pytest.raises(AssertionError):
        check_leap_year("hello")
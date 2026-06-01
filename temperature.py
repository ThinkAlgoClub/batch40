'''This module contains functions for temperature conversion.
As of now there are only two functions to convert between celsius and fahrenheit.
However, we will add more functions.'''

def to_celsius(fahrenheit):
    'This function converts fahrenheit to celsius'
    return (fahrenheit - 32) * 5 / 9

def to_fahrenheit(celsius):
    'This function converts celsius to fahrenheit'
    return celsius * 9/5 + 32

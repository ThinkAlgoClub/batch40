'''This is a module on tempeature related functions.
Currently we have coded two functions for temperature conversion.
Later we will add other functions and related components'''

def to_celsius(fahrenheit):
    'this function converts Fahrenheit to Celsius'
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    "This function converts Celsius to Fahrenheit"
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
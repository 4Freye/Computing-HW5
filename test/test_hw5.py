import pytest
import sys
import hw5
import unittest

# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#
class TestCarAtLight(unittest.TestCase):

    def test_car_at_light1(self):
        light1 = 'red'
        output = hw5.car_at_light(light1)
        expected_output = 'stop'
        assert output == expected_output

    def test_car_at_light2(self):
        light1 = 'blue'
        with self.assertRaises(Exception) as context:
            hw5.car_at_light(light1)

        self.assertTrue('Undefined instruction for color: {}'.format(light1) in str(context.exception))

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 

class TestSafeSubtract(unittest.TestCase):
    def test_safe_subtract1(self):
        a = 0
        b = 2
        output = hw5.safe_subtract(a,b)
        expected_output = -2
        assert output == expected_output
    
    def test_safe_subtract2(self):
        a = "f"
        b = 4
        output = hw5.safe_subtract(a,b)
        expected_output = None
        assert output == expected_output

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl
import datetime

class TestRetrieveAge(unittest.TestCase):
    def __init__(self):
        self.dict1 = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
        self.dict2 = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}

    def test_retrieve_age_eafp1(self):
        output = hw5.retrieve_age_eafp(self.dict1)
        expected_output = datetime.datetime.now().year - 1987
        assert output == expected_output

    def test_retrieve_age_eafp2(self):
        output = hw5.retrieve_age_eafp(self.dict2)
        expected_output = None
        assert output == expected_output

    def test_retrieve_age_lbyl1(self):
        output = hw5.retrieve_age_lbyl(self.dict1)
        expected_output = datetime.datetime.now().year - 1987
        assert output == expected_output

    def test_retrieve_age_lbyl2(self):
        output = hw5.retrieve_age_lbyl(self.dict2)
        expected_output = None
        assert output == expected_output

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#
import pandas as pd
class TestReadData(unittest.TestCase):
    def test_read_data(self):
        pathdf = 'sample_diabetes_mellitus_data.csv'
        output = hw5.read_data(pathdf)
        assert isinstance(output, pd.DataFrame)



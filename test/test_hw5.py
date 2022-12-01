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
    def setup(self):
        self.dict1 = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
        self.dict2 = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}

    def test_retrieve_age_eafp1(self):
        TestRetrieveAge.setup(self)
        output = hw5.retrieve_age_eafp(self.dict1)
        expected_output = datetime.datetime.now().year - 1987
        assert output == expected_output

    def test_retrieve_age_eafp2(self):
        TestRetrieveAge.setup(self)
        output = hw5.retrieve_age_eafp(self.dict2)
        expected_output = None
        assert output == expected_output

    def test_retrieve_age_lbyl1(self):
        TestRetrieveAge.setup(self)
        output = hw5.retrieve_age_lbyl(self.dict1)
        expected_output = datetime.datetime.now().year - 1987
        assert output == expected_output

    def test_retrieve_age_lbyl2(self):
        TestRetrieveAge.setup(self)
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


################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 

from functools import reduce

def count_simba(strings):
    return sum(map(lambda x: x.count('Simba'), strings))

def test_count_simba():
    x = 'Simba'
    output = count_simba(x)
    expected_output = 1
    assert output == expected_output

# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

def get_day_month_year(dates):
    data = list(map(lambda x: [x.day, x.month, x.year], dates))
    return pd.DataFrame(data, columns = ['day', 'month', 'year'])

import pandas as pd
import datetime
def test_get_day_month_year():
    x = [datetime.datetime(2022, 11, 28)]
    output = get_day_month_year(x)
    data = {'day':  [28],
            'month': [11],
             'year': [2022]
            }
    expected_output = pd.DataFrame(data)
    assert output == expected_output
    
# 8) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

from geopy import distance
from functools import reduce


def compute_distance(pairs):
    distances = []
    for pair in pairs:
        distances.append(reduce(lambda x,y: distance.distance(x,y).kilometers, pair))
    return distances

def test_compute_distance():
    x = [((41.23,23.5), (41.5, 23.4))]
    output = compute_distance(x)
    expected_output = 31.13186522205169
    assert output == expected_output

#################################################
# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
def sum_general_int_list(_list):
    s=0
    for x in _list: 
        if(isinstance(x,int)):
            s+=x
        elif(isinstance(x,list)):
            s+=sum_general_int_list(x)
    return s

def test_sum_general_int_list():
    x = [1,2,3]
    output = sum_general_int_list(x)
    expected_output = 6
    assert output == expected_output
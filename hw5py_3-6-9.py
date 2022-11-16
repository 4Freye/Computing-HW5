# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

def retrieve_age_eafp(dic):
    try:
        return dic['birth']
    except KeyError:
        print("The Dictionary doesn't have Birth key")
        
def retrieve_age_lbyl(dic):
    if 'birth' in dic:
        return dic['birth']
    else:
        print("The Dictionary doesn't have Birth key")  
        
################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
from functools import reduce
def count_simba(s):
    return s.upper().count("SIMBA")
result = reduce(lambda x,y:x+y,map(count_simba,ex))
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



from typing import List
"""
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 3
Exercise 4:

Use a lambda function for this exercise. Utilize map() Python function to implement a mapping 
for a list of integers to produce a new list in which each element is the result of the following 
functions for each corresponding element in the original list:

Example of your code execution: 
orig_list = range(10) 
new_list = list( map( mapping of the original list to the function above ) ) 
print(new_list) 

"""

def get_result(lst: List[int]):
    return list(map(lambda x: x**4 -4 * x**3 + 6* x**2 - 4 *x + 1, lst))
if __name__ == "__main__":
    print(get_result(range(10)))
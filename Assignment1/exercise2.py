from typing import List
"""
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 1 
Exercise 2:

Implement a function to compute cumulative sum of the values in numeric list. Name your 
function cum_sum(lst, limit), with two input parameters: lst is the list of numeric values, limit 
indicates up to which element in the list the sum is computed. Parameter limit should be optional 
and, if not specified, then the entire list should be used. The result should be returned from the 
function. 

An example of a using cum_sum() function: cum_sum(range(10)) 
And the expected output should be: 45 

An example of a using cum_sum() function: cum_sum(range(10), 4) 
And the expected output should be: 6 
"""

def cum_sum(lst: List[int], limit:int=0):
    if limit == 0:
        return sum(lst)
    
    c_sum = 0

    for idx, num in enumerate(lst):
        if idx == limit:
            break
        c_sum += num
    return c_sum

if __name__ == "__main__":
    print(cum_sum(range(10)))
    print(cum_sum(range(10), 4))
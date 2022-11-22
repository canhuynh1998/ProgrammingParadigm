from typing import List
"""
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 3
Exercise 2:

Using Python list comprehension, implement computing an intersection between two lists and 
save it in a third list. 

Example of your code execution: 

list1 = range(20) 
list2 = range(15, 30,1) 
list3 = [your code goes here] 
print(list3) 

Expected output: 
[15, 16, 17, 18, 19] 
"""

def find_intersection(lst1: List[int], lst2: List[int]):
    return [i for i in lst1 if i in lst2 ]

if __name__ == "__main__":
    print(find_intersection(range(20), range(15, 30, 1)))
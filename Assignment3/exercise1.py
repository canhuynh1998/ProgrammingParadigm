from typing import List
"""
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 3
Exercise 1:

Using Python list comprehension, implement list conversion from one numeric list to another 
list, which only contains those elements from the first list that are divided by 3 without 
remainder. 

Example of your code execution: 
list1 = range(30) 
list2 = [your code goes here] 
print(list2) 

Expected output: 
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
"""

def convert_list(lst: List[int]):
    return [i for i in lst if i % 3 == 0]

if __name__ == "__main__":
    print(convert_list(range(30)))
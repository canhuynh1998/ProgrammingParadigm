"""
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 5
Exercise 3:

Using Python list comprehension, implement processing of the following text: 

According to statistics, there are more trees on Earth than there are stars in the Milky Way. 
Today, there are around 3 trillion trees and 400 billion stars.  

You should compute a list that contains only words that are numeric values in the above text. 
Feel free to implement any helper functions for this exercise. At the end print the resulting list as 
follows: 
print(result) 

The expected output is: 
['3', '400'] 
"""

def get_numeric(string:str):
    return [n for n in string.split(" ") if n.isdigit()]

if __name__ == "__main__":
    print(get_numeric("According to statistics, there are more trees on Earth than there are stars in the Milky Way. Today, there are around 3 trillion trees and 400 billion stars. "))
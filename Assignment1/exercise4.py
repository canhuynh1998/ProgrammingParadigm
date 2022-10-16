from exercise3 import factorial
"""
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 1 
Exercise 4:

This exercise is an extension of the previous exercise. Write a function named 
multiple_factorials(n), where n is the maximum number for which the factorial is computed. A 
factorial should also be computed for each value less than n. The function does not return any 
value but instead print the result of each factorial computation on a separate line, starting from 
the largest number and going down to the output for factorial for 1. For any invalid input n the 
function should print “ERROR: invalid input”. In this exercise you should utilize the function 
you wrote for the previous exercise.  

An example of a using factorial() function: multiple_factorials(10) 
And the expected output should be: 

3628800 
362880 
40320 
5040 
720 
120 
24 
6 
2 
1 

An example of a using factorial() function: multiple_factorials(0) 
And the expected output should be: 
ERROR: invalid input

"""
def multiple_factorials(n:int):
    current_factor = factorial(n)
    if current_factor == -1:
        print("ERROR: invalid input")
        return
    else:
        while n > 0 :
            print(current_factor)
            current_factor //= n
            n-= 1

if __name__ == "__main__":
    multiple_factorials(10)
    multiple_factorials(0)
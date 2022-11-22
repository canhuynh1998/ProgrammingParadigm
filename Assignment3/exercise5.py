"""
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 3
Exercise 5:

Part1: 
For part 1, simply create closures named doubler and trippler create multiplier factories by 2 and 
3 correspondingly. Print the output of the doubler and trippler variables using value 3. 
Example of your code execution: 
doubler = make_multiplier(2) 
trippler = make_multiplier(3) 
print(doubler(3)) 
print(trippler(3)) 
The expected output is: 
6 
9 

Part2: 
For part 2, you will work with your implementation of make_multiplier() from part 1. Now use 
list comprehension to create a list of functions that multiply some value by a given factor. Simply 
use range(1,11,1) to create a list of factors. Your list of functions will contain functions as its 
elements, each function uses different factor to multiply a given value. Then use another list 
comprehension line of code to print values returned by these functions for values 3, 4, 5, and 6. 
In other words, the result of using the list of functions on each of these values should be another 
list.  
Example of your code execution: 
multiplier_list = [ your code goes here ] 
result3 = [ your code goes here ] 
result4 = [ your code goes here ] 
result5 = [ your code goes here ] 
result6 = [ your code goes here ] 
print(result3) 
print(result4) 
print(result5) 
print(result6) 
The expected output of using multiplier_list to make a list of results : 
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30] 
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40] 
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50] 
[6, 12, 18, 24, 30, 36, 42, 48, 54, 60] 

"""

def make_multiplier(n):
    def multiply(m):
        return m*n
    return multiply

def part1():
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(double(3))
    print(triple(3))

def part2():
    multiplier_list = [ i for i in range(1, 11) ] 
    result3 = [ make_multiplier(3)(i) for i in multiplier_list ] 
    result4 = [ make_multiplier(4)(i) for i in multiplier_list ] 
    result5 = [ make_multiplier(5)(i) for i in multiplier_list ] 
    result6 = [ make_multiplier(6)(i) for i in multiplier_list ] 
    print(result3) 
    print(result4) 
    print(result5) 
    print(result6) 
    
if __name__ == "__main__":
    part1()
    part2()
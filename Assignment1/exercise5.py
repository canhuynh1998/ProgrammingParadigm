"""
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 1 
Exercise 5:

This exercise will provide you with some practice with object oriented programming in Python. 
In this exercise you will work with a list of Student objects. Class Student is a child of class 
Person. Class Person has the following attributes: 
firstname 
lastname 
age 
Class Person also has a method named can_consume_alcohol(), which returns True if the student 
is of legal drinking age (21 years old), and False otherwise. Class Person also has two getters, for 
the first name and the last name. 
Class Student inherits from class Person and has the following additional attributes: 
gpa 
status 
Class Student has a getter named get_name(), which returns first and last name of the student 
concatenated together.  
Create a list of the following Student objects: 
Mike Smith, 21 yo, 3.7 gpa, Senior status 
Larry Mushroom, 19 yo, 2.1 gpa, Sophomore status 
Marry Wolf, 22 yo, 3.2 gpa, Senior status 
Tommy Tree, 20 yo, 3.5 gpa, Sophomore status 
Laura Tall, 21 yo, 3.1 gpa, Junior status 
Amy Paris, 18 yo, 3.9 gpa, Freshman status 

Part1: 
Iterate over the list of students and calculate how many are legal to drink alcohol. Output the 
computed value in the following format: 
Out of 6 students 3 are legal to consume alcohol. 

Part2: 
Tabulate and output how many students of each status are present in the list. Make sure to sort 
the output by the status. Most convenient way to implement this is with a dictionary. Iterate over 
the list and collect counts of each status representation in a dictionary, then sort this dictionary 
and print out its entries. Your output should look like this: 
Senior 2 
Junior 1 
Sophomore 2 
Freshman 1 

Part3: 
Sort your list of students by the gpa (in descending order) and output the students in the new 
sorted list in the following format: 
Amy Paris (3.9) 
Mike Smith (3.7) 
Tommy Tree (3.5) 
Marry Wolf (3.2) 
Laura Tall (3.1) 
Larry Mushroom (2.1) 

"""
from re import S
import string
from turtle import st
from typing import List


class Person:
    def __init__(self, firstname: string, lastname:string , age:int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def can_consume_alcohol(self):
        return self.age >= 21
    
    def get_firstname(self):
        return self.firstname
    
    def get_lastname(self):
        return self.lastname

class Student(Person):
    def __init__(self, firstname:string, lastname:string, age:int, gpa:float, status:string):
        super().__init__(firstname, lastname, age)
        self.gpa = gpa
        self.status = status
    
    def get_name(self):
        return self.get_firstname() + ' ' + self.get_lastname()

def part1Exercise5(students:List[Student]):
    print("Part 1:")
    count = 0
    output_format = "Out of {} students {} are legal to consume alcohol"
    for student in students:
        if student.can_consume_alcohol():
            count += 1
    print(output_format.format(len(students), count))

def part2Exercise5(students:List[Student]):
    print("\nPart 2:")
    status_count = {}
    for student in students:
        if student.status not in status_count:
            status_count[student.status] = 0
        status_count[student.status] += 1
    sorted_key = sorted(status_count.keys(), reverse=True)
   
    for key in sorted_key:
        status = ""
        if key == 1:
            status = "Freshman"
        elif key == 2:
            status = "Sophomore"
        elif key == 3:
            status = "Junior"
        else:
            status = "Senior"
        print(status, status_count[key])    

def part3Exercise5(students:List[Student]):
    print("\nPart 3:")
    sorted_students = sorted(students, key= lambda x: x.gpa, reverse=True)

    student_format = "{} ({})"
    for student in sorted_students:
        print(student_format.format(student.get_name(), student.gpa))

if __name__ == "__main__":
    students = [ 
        Student("Mike", "Smith", 21, 3.7, 4),
        Student("Larry", "Mushroom", 19, 2.1, 2),
        Student("Marry", "Wolf", 22, 3.2, 4),
        Student("Tommy", "Tree", 20, 3.5, 2),
        Student("Laura", "Tall", 21, 3.1, 3),
        Student("Amy", "Paris", 19, 3.9, 1),
        ]
    
    part1Exercise5(students)
    part2Exercise5(students)
    part3Exercise5(students)
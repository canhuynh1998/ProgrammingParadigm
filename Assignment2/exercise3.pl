/*
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 2 
Exercise 3

Implement a program that, given a list, outputs the value of the last element in that list. Name 
your rule get_last(List, E), where List is the list of elements, E is the variable that will hold the 
retrieved element. The query should return false for an empty list. 
An example of a query using this rule would be: 
get_last([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z], E). 
The expected output should be: z 
*/


get_last([X],X).
get_last([_|End],X) :- get_last(End,X).

/*
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 2 
Exercise 2

Implement a program that, given a list an element and an element value, outputs the index of that 
element in that list. If the element is not in the list, the query should output false. If there are 
multiple element values in the list, then the index of the first occurrence should be returned. 
Name your rule find(List, E, K), where List is the list of elements, E is the variable that will hold 
the retrieved element, and K is the index of the item to retrieve. Indexing should start with 1 for 
this exercise.  

An example of a query using this rule would be: 
find([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z], a, K). 

The expected output should be: 1 
An example of a query using this rule would be: 
find([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z], b, K). 
The expected output should be: 2 

An example of a query using this rule would be: 
find([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z], 9, K). 
The expected output should be: false 
*/

find([E|_], E, 1).
find([_|List], E, IDX):- find(List, E, IDX1),IDX is IDX1+1.
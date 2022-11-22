/*
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 2 
Exercise 4

Implement a program that, given two lists, outputs true if all the elements of the first list are in 
the the second list, otherwise outputs false. Name your rule members(List1, List2), where List1 
is the first list, List2 is the second list.  
An example of a query using this rule would be: 
members([a,d,h],[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]). 
The expected output should be: true 
An example of a query using this rule would be: 
members([a,d,8],[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]). 
The expected output should be: false 
An example of a query using this rule would be: 
members([],[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]). 
The expected output should be: true 
*/

members(X, [X|_]).
members(X, [_|Yend]) :- members(X, Yend).
members([], _).
members([X|Xend], Y) :- members(X,Y), members(Xend, Y).
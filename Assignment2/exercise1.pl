
% CS152 Fall 2022
% Hoc Can Huynh
% 014836757
% Homework assignment 2 
% Exercise 1
% Implement a program that, given a list and an index k, outputs k’s element in that list. Name your 
%rule get_i(List, K, E), where List is the list of elements, K is the index of the item to retrieve, and 
% E is the variable that will hold the retrieved element. Indexing should start with 1 for this 
% exercise. 
% An example of a query using this rule would be: 
% get_i([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z], 3, E). 
% And the expected output should be: c 
% If the index is out of bounds the query should return false. 


get_i([A|_],1,A).
get_i([_|LIST],IDX,E):- IDX>1,IDX1 is IDX-1,get_i(LIST,IDX1,E).
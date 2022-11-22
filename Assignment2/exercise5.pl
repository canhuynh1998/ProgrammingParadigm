/*
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 2 
Exercise 5

Remember our Prolog examples where we defined family relationships? Consider the following 
family (you can copy and paste these relationships into your program): 
father_of(jose, david). 
father_of(nicolas, david). 
father_of(laura, david). 
father_of(tina, david). 
father_of(ricky, nicolas). 
father_of(mateo, nicolas). 
father_of(moira, greg). 
father_of(trevor, bruce). 
father_of(lisa, bruce). 
father_of(mary, jose). 
father_of(john, jose). 
mother_of(ricky, lena). 
mother_of(jose, lupe). 
mother_of(nicolas, lupe). 
mother_of(laura, lupe). 
mother_of(tina, lupe). 
mother_of(mateo, lena). 
mother_of(moira, laura). 
mother_of(trevor, tina). 
mother_of(lisa, tina). 
mother_of(mary, cassandra). 
mother_of(john, cassandra). 
For this exercise you are asked to define a rule that returns true of the two persons are first-
cousins. Below is the chart for your information that gives definitions of different family 
relationships, including first-cousin relationship to a given individual: 
Image on canvas

Name your rule first_cousin(A, B), where A is the first individual (e.g. john), B is the second 
individual (e.g. moira).  
An example of a query using this rule would be: 
first_cousin(john, X). 
The expected output should be: 
Image on canvas

For this exercise you can implement additional “helper” rules that will make the first_cousin rule 
easier to code and more compact. Depending on how you implement your rule(s) you might 
notice duplicate values returned by the first_cousin query. That is because Prolog keeps track of 
all variable, including free variables. You can incorporate distinct() function into your query:  
distinct( first_cousin(john, X)).
*/

father_of(jose, david). 
father_of(nicolas, david).
father_of(laura, david).
father_of(tina, david).
father_of(ricky, nicolas).
father_of(mateo, nicolas).
father_of(moira, greg).
father_of(trevor, bruce).
father_of(lisa, bruce).
father_of(mary, jose).
father_of(john, jose).

mother_of(ricky, lena).
mother_of(jose, lupe).
mother_of(nicolas, lupe).
mother_of(laura, lupe).
mother_of(tina, lupe).
mother_of(mateo, lena).
mother_of(moira, laura).
mother_of(trevor, tina).
mother_of(lisa, tina).
mother_of(mary, cassandra).
mother_of(john, cassandra).

parent_of(A,B):-father_of(A,B) ; mother_of(A,B).
first_cousin(A, B):-parent_of(A,X), parent_of(B,Y),X \== Y,parent_of(X,C),parent_of(Y,C).
"""
CS152 Fall 2022
Hoc Can Huynh
014836757
Homework assignment 1 
Exercise 1:

Michael is searching for a job and is applying to various companies. He has some restrictions 
though. He loves the west coast of the US (the states of California, Oregon, Washington) and will 
accept any position that pays over $80,000/year in those states. In order to accept a job in another 
state, he wants an offer of at least least $100,000 a year. He also is not willing to move to some 
states: Arizona, New Mexico, and Texas. It is too hot for his liking in those states. He is not 
willing to accept any offer in those three states.   
Michael wants to automate the process of selecting companies to which he will apply. Your task 
is to help Michael by implementing a function named select_company(state, salary), which 
accepts two input parameters: state and salary the position pays. This function will return either 
true or false, indicating whether Michael should apply to this company or not. Use conditionals 
to implement the logic flow for whether Michael should send in an application for a given 
position. 

An example of a using select_company() function: select_company(“California”, 85000) 
And the expected output should be: True 

An example of a using select_company() function: select_company(“New Mexico”, 160000) 
And the expected output should be: False 

An example of a using select_company() function: select_company(“Colorado”, 110000) 
And the expected output should be: True 
"""

def select_company(state: str, salary: int):
    if state == 'California' or state == 'Oregon' or state == 'Washington':
        if salary > 80000:
            return True
        return False
    if state == 'Arizona' or state == 'New Mexico' or state == 'Texas':
        return False
    
    if salary >= 100000:
        return True
    return False

if __name__ == "__main__":
    print(select_company("Arizona", 200000))
    print(select_company("Texas", 200000))
    print(select_company("New Mexico", 200000))
    print(select_company("California", 200000))
    print(select_company("Oregon", 200000))
    print(select_company("Washington", 200000))
    print(select_company("California", 80000))
    print(select_company("Oregon", 80000))
    print(select_company("Washington", 80000))
    print(select_company("California", 85000))
    print(select_company("Oregon", 85000))
    print(select_company("Washington", 85000))
    print(select_company("New York", 110000))
    print(select_company("Idaho", 80000))
    print(select_company("Rhode Island", 20000))
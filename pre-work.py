#Question 1
#Write a function to print "hello_USERNAME!" 
def hello_name(user_name):
    print("hello_"+user_name.upper()+"!")

#Question 2 
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for numbers in range(1,100):
        if numbers % 2 >=1:
            return(numbers)

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    for items in a_list:
        print(max(a_list))
        return

#Question 4 
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    a_year = int(a_year)
    if (a_year % 400 == 0):
        return True
    elif (a_year % 100 == 0):
        return True
    elif (a_year % 4 == 0):
        return True
    else:
        return False

# Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    for num in a_list:
        if  num == a_list[0]:
            consec = num+1
        elif num == consec:
            consec += 1
        else:
           return(print("Nonconsecutive"))
    print("Consecutive")
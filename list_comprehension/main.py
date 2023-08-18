numbers = [1,2,3]
new_list = [n + 1 for n in numbers]
print(new_list)
name = "Anish"
#Doesn't only mean that we should work with lists. We can also work with Strings.

letters_list =  [letter for letter in name]
#These things are known as sequences

range(1,5)
new_list1 = [n*2 for n in range(1,5)]
print(new_list1)

#Conditional List Comprehension
names = ["Anish", "Garv", "Aditya", "Gaurav"]
print (names[2])

short_names = [name for name in names if len(name) < 5]
print(short_names)

upper_case_names = [name.upper() for name in names if len(name) > 5]
print(upper_case_names)


#List comprehension exercise:

import time
import datetime

current_date = datetime.datetime.now()
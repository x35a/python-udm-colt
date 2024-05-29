# Types
# bool # True or False
# int # integer
# float # float number
# str # string
# list # an ordered sequence of values of other data types eg. [1,2,3] or ["a","b"]
# dict # a collection of key: values {"a": 1, "b": 2}
# None # used to signify the absence of a value in many situations, e.g., it is returned from functions that don’t explicitly return anything. Its truth value is false. https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/9141982#overview

# Built-in Types https://docs.python.org/3.12/library/stdtypes.html
# types https://www.w3schools.com/python/python_datatypes.asp

# type() # check type

# multiple variable assignment
# all, at, once = 5, 10, 15
# 5.23 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8680072#overview

# Numbers
# division always returns a floating point number
# print(5/1) # 5.0
# https://docs.python.org/3.12/tutorial/introduction.html#numbers
# 1.25 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8680038

# Strings
# F-Strings
# val = 10
# text = f"text {val + 1}"
# https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8680138#overview

# string methods https://docs.python.org/3.12/library/stdtypes.html#string-methods

# number + string = error
# - / ops not working
# BUT
# * works as str repiter # print('abc' * 10) # prints 'abc' 10 times
# 2.00 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8680110#overview

# Get char by string index
# 'abc'[1] # b
# 'abc'[-1] # c
# 'abc'[4] # error: string index out of range

# Functions to convert types
# int(12.56) # 12
# str([1,2,3]) # '[1,2,3]'
# float()
# 2.36 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8680116#overview

# Don't name variables like: int, str or any buildin function like int(), str(), otherwise error on func call: 'str' object is not callable.
# 5.00 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8680116#overview

# round(thing to round, how many decimal points) # to round a number

# input() # waits user input from terminal
# inputText = input('Enter your text:')
# 3.30 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8680130#overview
# 1.00 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/7990986#overview

# Conditionals
# name = ''
# if name == 'a':
#   print('a')
# elif name == 'b':
#   print('b')
# else:
#   print('c')
# https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/7990998#overview

# Conditional checks
# Condition is False if: empty object, '', 0, None, False
# vid 66
# Truth Value Testing https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# Comparison operators
# <, >, <=, >=, ==, !=
# vid 67
# comparison btwen int and float works
# comparison btwen int and string does not work
# `is` vs `==` https://replit.com/@35795/python-udm-colt#is_vs_==.py

# Logical operators
# and, or, not
# vid 68, 70

# print('abc\n * 10) # sting repiter
# 7.55 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8747976#reviews

# переменная обьявленная внутри if видна за его пределами
# 4.13 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8747986#overview

# import random # imports module and its methods
# a = random.randint(1,10)
# from random import randint # imports only randint method
# a = randint(1,10)
# 10.05 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8747986#overview

# for item in iterable_object:
#    do smth with item
# string is also iterable_object btw
# https://docs.python.org/3.12/reference/compound_stmts.html#the-for-statement
# https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/7991008#overview

# range(start, stop, step)
# represents an immutable sequence of numbers, commonly used for looping
# it's a range data type but if wrap in list() it's a list type
# type(range(3)) # range type
# list(range(3)) # [0,1,2]
# ranges https://docs.python.org/3.12/library/stdtypes.html#ranges
# https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8814020#overview

# while expression_is_true:
# n = 0
# while n < 3:
#   print(n)
#   n += 1
#   # break and continue are optional
# else: # optional
#   print('end') # do some code if expression is false and terminate the loop
# https://docs.python.org/3.12/reference/compound_stmts.html#the-for-statement
# https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/7991014#overview

# Lists
# vid 97-110
# Lists are mutable sequences, typically used to store collections of homogeneous items.
# https://docs.python.org/3.12/library/stdtypes.html#lists
# Common Sequence Operations https://docs.python.org/3.12/library/stdtypes.html#common-sequence-operations
# Mutable Sequence Operations https://docs.python.org/3.12/library/stdtypes.html#mutable-sequence-types

# len([a,b,c]) # 3 # returns list length
# len(range(3)) # 3 # returns range
# list(range(1, 100)) # list of numbers from 1 to 99
# somelist[index] # accesses list item at index
# somelist[-1] # negative number to index backwards
# 2.50 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/7991020#questions
# Check if a value is in a list
# 'a' in ['a', 'b', 'c'] # True
# https://docs.python.org/3.12/library/stdtypes.html#common-sequence-operations
# 3.40 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/7991020#questions

# iterating over lists
# vid 102
# colors = ['red', 'green', 'blue']
# for color in colors # loop through list
# while loop

# list methods
# .append() # adds item to end of list
# .extend() # adds items to end of list
# .insert(index, item) # adds item to index of list
# .insert(len(list), item) # adds item to end of list
# .clear() # removes all items from list
# .pop() # removes last item from list
# .pop(1) # removes item at index 1
# .remove(item) # removes item from list
# .index(item, x, j) # returns index of item in list
# .sort() # sorts list in place
# https://docs.python.org/3.12/library/stdtypes.html#list.sort
# list to string using string method .join()
# ','.join(['a', 'b', 'c']) # a,b,c

# list slicing (more investigation is needed)
# newlist = list[0:] # copy the list (probably shallow)
# slicing doesn't change the original list
# 4.00 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/7991022?start=15#questions

# ls1 = ['a', 'b', 'c', 'd']
# ls2 = ls1
# ls3 = ls1[0:]
# ls4 = ls1[2:3]
# print(ls2 is ls1) # true
# print(ls3 is ls1) # fasle
# print(ls4 is ls1) # fasle

# s[i:j] # returns list from index i to j-1
# s[i:j:k] # returns list from index i to j-1 with step k
# s[i:] # returns list from index i to end
# s[:j] # returns list from start to j-1]

# ls1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(ls1[1:3]) # b, c
# print(ls1[:3]) # a, b, c
# print(ls1[1:]) # b, c, d
# print(ls1[1:4:2]) # b, d
# print(ls1[10:20]) # []
# print(ls1[10:]) # []
# print(ls1[-1]) # d
# print(ls1[-3:]) # b, c, d
# print(ls1[-3:-1]) # b, c
# print(ls1[-4:-1:2]) # a, c
# print(ls1[-10:]) # a, b, c, d
# print(ls1[-10:-7]) # []
# print(ls1[:-10]) # []
# print(ls1[::-1]) # d, c, b, a # -1 step means reverse
# print(ls1[0:3:-1])  # []
# print(ls1[2:0:-1]) # c, b
# print(ls1[1::-1])  # b, a
# print(ls1[:1:-1])  # d, c

# modify portions of list
# numbers = [1, 2, 3, 4, 5]
# numbers[1:3] = [10, 20] # replaces 2 and 3 with 10, 20

# swappin values
# https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8845920#overview
# ls = ['a', 'b']
# ls[0], ls[1] = ls[1], ls[0] # [b, a]]

# List Comprehesion
# List comprehensions provide a concise way to create lists.
# https://docs.python.org/3.12/tutorial/datastructures.html#list-comprehensions
# vid 112-121 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/7991024#overview

# nums = [1, 2, 3]
# numsx2 = [x * 2 for x in nums]  # [2, 4, 6]
# print(numsx2)
# numsx2 = [x * 2 for x in nums if x > 1] # syntax error if put 'else' after 'if' stment
# print(numsx2)  # [4, 6]

# Ternary Operator
# print([num * 2 if num % 2 == 0 else num / 2 for num in nums])  # [0.5, 4, 1.5]
# https://www.w3schools.com/python/python_conditions.asp
# 1.00 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8377510#overview

# list to string + filter out some chars
# with_vowels = 'This is so much fun!'
# print(''.join(char for char in with_vowels if char not in 'aeiou')) # Ths s mch fn!


# Nested Lists
# https://docs.python.org/3.12/tutorial/datastructures.html#nested-list-comprehensions
# https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/7991026#overview

# nested list access
# nested_list = [[1,2,3], [4,5,6], [7,8,9]]
# nested_list[0][1] # 2
# nested_list[-1] # [7,8,9]

# read nested list in a row
# [[print(val) for val in k] for k in nested_list] # 1 2 3 4 5 ..

# generate nested list
# [[k for k in range(1,4)] for i in range(3)] # [[1,2,3], [1,2,3], [1,2,3]]

# with if else
# [['X' if k%2 != 0 else 'O' for k in range(1,4)] for i in range(3)] # [['X', 'O', 'X'], ['X', 'O', 'X'] .. ]
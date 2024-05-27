# Types
# bool # True or False
# int # integer
# float # float number
# str # string
# list # an ordered sequence of values of other data types eg. [1,2,3] or ["a","b"]
# dict # a collection of key: values {"a": 1, "b": 2}
# None # used to signify the absence of a value in many situations, e.g., it is returned from functions that don’t explicitly return anything. Its truth value is false. https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/9141982#overview

# Built-in Types https://docs.python.org/3.12/library/stdtypes.html

# type() # check type

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
# Lists are mutable sequences, typically used to store collections of homogeneous items.
# https://docs.python.org/3.12/library/stdtypes.html#lists
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
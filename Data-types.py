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


# number + string = error (or any math operator)
# 2.00 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8680110#overview


# Strings
# F-Strings
# val = 10
# text = f"text {val + 1}"
# https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8680138#overview


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


# input() # waits user input from terminal
# 3.30 https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/8680130#overview


# round(thing to round, how many decimal points) # to round a number
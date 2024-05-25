# is vs ==
# vid 71

# == operator checks if the values of two variables are equal. (Equality Operator)
# is operator checks if two variables are the same object, i.e., they have the same memory address. (Identity Operator)

a = 1
b = 1
c = 1.0
d = '1'

x = [1, 2, 3]
y = [1, 2, 3]

k = {a: 1, b: 2}
n = {a: 1, b: 2}

# print(a == a)  # true because the same value
# print(a == b)  # true because the same value
# print(a == 1)  # true because the same value
# print(a == c)  # true because both a and c are numeric types (integer and float, respectively), and Python allows comparison between different numeric types. So, even though a is an integer and c is a float, Python can compare their values and determine that they are equal.
# print(a == d)  # false because a is an integer and d is a string. Python does not allow direct comparison between an integer and a string.

# print(a is a)  # true because the same object
# print(a is b)  # true because a and b are both integers with the same value, so they can be the same object. Python has an optimization feature for small integers (-5 to 256), where it reuses the same object for the same value. Therefore, a is b can be True. However, this is an implementation detail and not guaranteed by the language, so it's generally safer to use == to compare values.
# print(a is c)  # false because a is an integer, while c is a float. Python treats integers and floats as different types of objects, even if their values are the same.
# print(a is d)  # false because not the same object
# print(a is 1)  # true but - SyntaxWarning: "is" with a literal. Did you mean "=="? #SyntaxWarning for a is 1 because the is operator is generally used to compare variables with objects in memory. It's not recommended to use it with literal values.

# print(x == x)  # true
# print(x == y)  # true
# print(x == [1, 2, 3])  # true
# all above is True because all values are equal

# print(x is x)  # true
# print(x is y)  # false
# print(x is [1, 2, 3])  # false

# print(k == k)  # true
# print(k == n)  # true
# print(k == {a: 1, b: 2})  # true

# print(k is k)  # true
# print(k is n)  # false
# print(k is {a: 1, b: 2})  # false

# Correct the following invalid variable names and explain why they’re invalid:
# 1st_name = "Raj"
# class1 = "B.Tech"            # reserved keywords cannot be the variable name
# full-name = "Raj Kumar"
# print(1st_name, class, full-name)
# ...............................................................................

# Convert the following into valid multi-word variable names:
# total_marks_of_student=5687
# isstudent-present-today=True
# Average-Score=89

# ...............................................................................
"""
Task to print the following information
- Name => String
- Age => Int
- Gender => String
- has_driving_license => Boolean
- citizen_of_india => Boolean
- salary => Float
"""
# ...............................................................................
# IMPLICIT TYPE CASTING
# x = 90
# print(type(x))  # int
# x = "we"
# print(type(x))
# x = 89.60
# print(type(x))

# ..............................................................................
# EXPLICIT TYPECASTING

# y = 98
# print(y, type(y))
# z = float(y)
# print(z, type(z))

# a = -78
# c = 0
# print(a, type(a))
# print(bool(a), a)
# print(bool(c), c)  # 0 => False
# b = "Sam"
# print(bool(b))
# print(bool(""))  # Empty String changes to False
# d = "34"
# e = int(d)
# f = float(d)
# print(e, type(e), f)
# ................................................................................
# Multiple Values to multiple Variable

# x = 23
# y = 56
# z = 67
# print(x, y, z)
# x, y, z = 23, 56, 67
# print(x, y, z)
# ................................................................................
# One value to multiple variables

# a = 1
# b = 1
# c = 1
# print(a, b, c)

# a = b = c = 1
# print(a, b, c)
# ................................................................................

# Mathematical Operators
# Addition + =>
a = 2
b = 9
print(a + b)
# Subtraction - =>
a = 2
b = 9
print(b - a)
# Multiplication * =>
a = 2
b = 9
print(b * a)
# Division / =>
a = 3
b = 9
print(b / a)
# Modulo % =>   gives the remainder
a = 2
b = 9
print(b % a)
# Exponentiation Operator ** => compute the power of any number
a = 3
b = 2
print(a**b)  # 3^2 => 3*3

q = 9
r = 2
print(q * r, q**r)  # 18, 81
# ............................................
# Maths => 98
# Science => 56
# Social Science => 90
# Print Total Marks
# Print Average Marks
# ..........................................................
d = 3
e = 2
f = 4
sum = (d * 2) + (e * 2) + (f * 2)
print(sum)  # 18
# ............................................................
# String Concatenation
x = 1
y = 2
p = "Hi..."
q = "Sam..."
print(x + y)  # 3
print(p + q)  #
# ...........................................................

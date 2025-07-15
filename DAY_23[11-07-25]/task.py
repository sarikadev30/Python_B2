# Fibonacci Series
# 0 1 1 2 3 5 8 13 21 34


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c


fibonacci(5)
# fibonacci(5):
# a=0 b=1
# i=0 => P(a)=>0    c=0+1=1  a=1   b=1
# i=1 => P(a)=>1    c=1+1=2  a=1   b=2
# i=2 => P(a)=>1    c=1+2=3  a=2   b=3
# i=3 => P(a)=>2    c=2+3=5  a=3   b=5
# i=4 => P(a)=>3    c=3+5=8  a=5   b=8
# i=5 => For Loop Terminates

# ................................................................
# Create a function multiply_list(lst) that returns the product of all elements in a list.

# ......................................................................................
# Difference between Print and Return in the function


# def fun(a, b):
#     # print(a * b)
#     return a * b
# # fun(3, 4)
# print(fun(3, 4))
# ........................................................................................
# Create a function multiply_list(lst) that returns the product of all elements in a list.


def multiply_list(lst):
    print("lst", lst)


a = [1, 2, 3, 4, 5]
print("a", a)
multiply_list(a)

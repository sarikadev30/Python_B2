# 0 1 1 2 3
# def fibonacci(n):
#     a = 0
#     b = 1
#     res = []
#     for i in range(n):
#         res.append(a)
#         c = a + b
#         a = b
#         b = c
#     # print(res)
#     return res


# x = fibonacci(5)
# print(x)

# print(fibonacci(5))

# ...................................................................
# SCOPE
#  Local Scope
#  Enclosing Scope
#  Global Scope
#  Built in Scope


# Local Scope
# def greet():
#     x = "Sam"  # Local Scope
#     print(f"Good Evening {x}")
#     print(x)


# greet()
# print(x)

# ............................................................................
#  Enclosing Scope
# def outer():
#     x = "Sam"

#     def inner():
#         nonlocal x
#         x = "Leo"
#         xy = "Danny"
#         print(xy)
#         print(x)

#     inner()
#     print(x)


# outer()
# ...........................................................................
# Global Scope
# x = 34


# def greet2():
#     global x
#     x = 90
#     print(x)


# print(x)
# greet2()
# print(x)
# ............................................................................
# Built in Scope

# y = len("Python")
# print(y)

# ...........................................................................


# Problems

# x = 10  # x=10  Global Scope


# def my_func():
#     x = 20  # x=20 Local Scope
#     print(x)


# my_func()
# print(x)

# A=> 10 20
# S=> 20 10
# ..............................................................................

# x = 100  # x=100 Global Scope   x=200


# def change():
#     global x
#     print(x)  # 100
#     x = 200
#     print(x)  # 200


# change()
# print(x)  # 200

# A=> 200 200 100
# S=> 200 200 100
# ................................................................................


# x = 5  # Global Scope => x=5


# def outer():
#     # x = 10                # Local Scope x=10
#     def inner():
#         print(x)  # 10
#     inner()

# outer()
# print(x)  # 5

# S=> 10 5
# A=> 10 5
# ...............................................................................

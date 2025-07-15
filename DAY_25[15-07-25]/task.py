# ............................................................
# def func():
#     print(x)


# x = 50
# func()

# A=>
# S=>

# ...........................................................

# x = 10
# y = 78
# print(y)  # 78


# def func():
#     global x
#     print(x)  # 10
#     x = 20
#     print(x)  # 20


# func()
# print(x)
# ...........................................................

# x = "global"


# def outer():
#     x = "outer"

#     def inner():
#         print("inner:", x)

#     inner()
#     print("outer:", x)


# outer()
# print("global:", x)

# S => inner : outer  outer: outer    global:global
# ..............................................................

"""
Count Words in a Sentence
**Problem Statement:**
Write a function `count_words` that takes a sentence and returns the number of words.
print(count_words("I love Python programming"))  # Output: 4

"""


# def count_words(sent):
#     ans = sent.split(" ")
#     return len(ans)


# print(count_words("I love Python programming"))

"""
Convert Celsius to Fahrenheit
**Problem Statement:**
Write a function `to_fahrenheit` that converts a temperature in Celsius to Fahrenheit.
Fahrenheit = Celsius × 9/5 + 32
print(to_fahrenheit(0))   # Output: 32.0
print(to_fahrenheit(100)) # Output: 212.0

"""

# def to_fahrenheit(c):
#     f = c * 9 / 5 + 32
#     return f

# print(to_fahrenheit(0))
# print(to_fahrenheit(100))
# .........................................................................................
"""
Check if List is Empty
**Problem Statement:**
Write a function `is_empty` that checks if a list is empty.
print(is_empty([]))      # Output: True
print(is_empty([1, 2]))  # Output: False
"""


# def is_empty(lst):
#     if len(lst) == 0:
#         return True
#     else:
#         return False


# print(is_empty([]))
# print(is_empty([1, 2]))

# ................................................................................................
"""
Repeat a String
**Problem Statement:**
Write a function `repeat_string` that takes a string and number `n` and returns the string repeated `n` times.
print(repeat_string("hi", 3))  # Output: "hihihi"
"""


# def repeat_string(s, n):
#     x = ""
#     for i in range(n):
#         x += s
#     return x


# print(repeat_string("hi", 3))

# ........................................................................
"""
Count Positive and Negative Numbers
**Problem Statement:**
Write a function `count_pos_neg` that takes a list and returns the count of positive and negative numbers.
print(count_pos_neg([1, -2, 3, -4, 5]))  # Output: [3, 2]
"""
# def count_pos_neg(lst):
#     res = []
#     cp = cn = 0
#     for i in lst:
#         if i > 0:
#             cp += 1
#         elif i < 0:
#             cn += 1
#     res.append(cp)
#     res.append(cn)
#     return res

# print(count_pos_neg([1, -2, 3, -4, 5]))

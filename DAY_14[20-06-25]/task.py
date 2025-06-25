# for i in range(3):  # 0 1 2
#     for j in range(3):  # 0 1 2
#         print(i, j)


"""
******
******
******
******
"""
# n = 4
# for i in range(n):  # 0 1 2 3
#     for j in range(6):  # 0 1 2 3 4 5
#         print("*", end="")
#     print()

"""
123456
123456
123456
123456
"""

# n = 4
# for i in range(n):  # 0 1 2 3
#     for j in range(6):  # 0 1 2 3 4 5 or (1,7)
#         print(j + 1, end="")
#     print()


"""
111111
222222
333333
444444
"""
# n = 4
# for i in range(1, n + 1):  # 0 1 2 3
#     for j in range(6):  # 0 1 2 3 4 5
#         print(i, end="")
#     print()

"""
*
**
***
****
*****
"""

# i => 0 1 2 3 4  j => 1 2 3 4 5  j= i+1
# i => 1 2 3 4 5  j => i
# n = 5
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()

"""
*****
****
***
**
*
"""

# n = 5
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()

"""
1
12
123
1234
12345
"""
# n = 5
# for i in range(1, n + 1):
#     for j in range(i):
#         print(j + 1, end="")
#     print()

"""
1
22
333
4444
55555
"""
# n = 5
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end="")
#     print()

"""
12345
1234
123
12
1
"""
# n = 5
# for i in range(n, 0, -1):
#     for j in range(i):
#         print(j + 1, end="")
#     print()
"""
55555
4444
333
22
1
"""
# n = 5
# for i in range(n, 0, -1):   # 5 4 3 2 1
#     for j in range(i):       # 5 4 3 2 1
#         print(i, end="")
#     print()

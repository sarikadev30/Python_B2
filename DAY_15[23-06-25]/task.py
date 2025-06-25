# Patterns

"""
# Hollow Square Pattern
*****
*   *
*   *
*   *
*****

*****
*...*
*...*
*...*
*****
"""
#  i=0 i=4 j=0 j=4
# n = 5
# for i in range(n):  # 0 1 2 3 4
#     for j in range(n):  # 0 1 2 3 4
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

"""
    *
   ***
  *****
 *******
*********

....*
...***
..*****
.*******
*********
"""
# n=5
#           j=(n-i)     k=2*i-1    2*i-1-1 (2*i-2)
# i=1       j=4         k= 1          => 0
# i=2       j=3         k= 3          => 0 1 2
# i=3       j=2         k= 5          => 0 1 2 3 4
# i=4       j=1         k= 7
# i=5       j=0         k= 9
# i=6

n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()

"""
*********
.*******
..*****
...***
....*

"""
# n = 5
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()


"""
    *
   *#*
  *###*
 *#####*
*********
"""

# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):  # 2*i-1-1=> 2*i-2      5 => 0 1 2 3 4
#         if k == 0 or i == n or k == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

"""
....1
...1 2
..1 2 3
.1 2 3 4
1 2 3 4 5
"""
# n=5
#           j=(n-i)     k=i
# i=1       j=4         k=1
# i=2       j=3         k=2
# i=3       j=2         k=3
# i=4       j=1         k=4
# i=5       j=0         k=5
# i=6

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

"""
A
BB
CCC
DDDD
EEEEE
"""
# 65 => A   66 =>B
x = 65
print(chr(x))

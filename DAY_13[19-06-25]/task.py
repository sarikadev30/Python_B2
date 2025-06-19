# ...............................................................................
# Revision
# 1-2+3-4+5-6+7......N

# n = 4
# sum = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sum -= i
#     else:
#         sum += i
#     # print(i, sum)

# print(sum)

# i=1 sum=0+1=1
# i=2 sum=1-2=-1
# i=3 sum=-1+3=2
# i=4 sum=2-4=-2
# i=5 => Sum => -2
# ...............................................................................
# Nested Loop

# Problem 1 : Father gave the son a target, of completing 10 sets. Each set contains 10 Rounds of a field.
# Set 1 round 1
# Set 1 round 2
# Set 1 round 3

# for i in range(1, 6):
#     for j in range(1, 5):
#         print(i, j)

# 1 2 3 4 5
# 1 2 3 4

# 1 => 1 2 3 4
# 2 => 1 2 3 4
# 3 => 1 2 3 4
# 4 => 1 2 3 4
# 5 => 1 2 3 4
# 6

"""
**********
**********
**********
**********
**********

"""
# n = 5
# for i in range(n):
#     for j in range(10):
#         print("*", end="")
#     print()

# i=0 j=0   => j=9  **********
# i=1 j=0   => j=9  **********
# i=2 j=0   => j=9  **********
# i=3 j=0   => j=9  **********
# i=4 j=0   => j=9  **********
# i=5

"""
12345678
12345678
12345678
12345678
12345678

*                    i=1 j=1
**                   i=2 j=2
***
****
*****

1
12
123
1234
12345

1
22
333
4444
55555

"""
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()

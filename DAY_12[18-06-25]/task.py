#  Arithematic Progression Series

# 1,2,3,4,5,6,7,8,9.............
# 1, 1+1=2, 2+1=3, 3+1=4

# 2,4,6,8,10,12
# 2 2+2=4, 4+2=6


# a=2   d=2 n=6
# 1st term => a = 2
# 2nd term => a+d => 2+2 =4
# 3rd term => 2nd term + d = a+d+d = a+2*d => 2+2*2=6
# 4th term => 3rd term + d = a+2*d+d = a+3*d => 2+3*2=8

# a=2 d=2 n=4  => sum
# 2,4,6,8


#  a=1 d=3 n=4
# 1,4,7,10
#  1st t => a+0*d =1
#  2nd t => a+d => 1+3= 4
#  3rd t => 2nd t + d => a+d+d=a+2*d = 1+2*3= 7
#  4th t => 3rd t + d => a+3*d= 1+3*3=10

# a = 1
# d = 3
# n = 4
# 1,4,7,10
# a = int(input("Enter a number(a):"))
# d = int(input("Enter a number(d):"))
# n = int(input("Enter a number(n):"))
# sum = 0
# for i in range(n):
#     x = a + i * d
#     sum += x
#     print(x, sum)
# print(sum)

# a=1 d=3 n =4
# i=0 => x= a+i*d => 1+0*3 => 1
# i=1 => x=a+1*d => 1+1*3=> 1+3 = 4
# i=2 => x=a+2*d => 1+2*3=> 1+6 = 7
# i=3 => x=a+3*d => 1+3*3=> 1+9 =10

# ...................................................................
#  Geometric Progression
# a= first term, r=common ratio, and n=number of terms.

# a = 1
# r = 2
# n = 4
# # a2= a*r = 1*2 = 2
# # a3= a2*r => a*r*r => a*r**2 = 1*2*2 =>4
# # sum = 0
# for i in range(n):
#     x = a * r**i
#     # sum += x
#     print(x)

# .......................................................................
#  Nested Loop
# for family in range(1, 6):
#     for candy in range(1, 5):
#         print(family, " ate ", candy, " candy")

# for i in range(3):
#     for j in range(2): 0,1
#         print("Hello")

# i = 0

# while i < 3:
#     j = 0
#     while j < 2:
#         print("Hello", i, j)
#         j += 1
#     i += 1

# i => 0 ,1, 2
# j => 0 ,1

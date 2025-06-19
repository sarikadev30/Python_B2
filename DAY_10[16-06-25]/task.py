# Print the average of even numbers from 1 to 100 (both included)
# count = 0
# total = 0
# number = 1
# while number <= 6:
#     if number % 2 == 0:
#         total += number
#         count += 1
#     number += 1

# average = total / count
# print(average)

# ..................................................
# c=0 t=0 n=1
# n=1 n=>odd  n=1+1=2
# n=2 n =>even t=0+2=2 c=0+1=1 n=2+1=3
# n=3 n=>odd  n=3+1=4
# n=4 n=>even t=2+4=6 c=1+1=2 n=4+1=5
# n=5 n=>odd n=5+1=6
# n=6 n=>even t=6+6=12 c=2+1=3 n=6+1=7
# n=7 FALSE
# average= 12/3 => 4.0
# ..................................................................

# BREAK
# n = 1
# while n <= 6:
#     if n == 3:
#         break
#     print(n)
#     n += 1
# print("End")
# n=1 1<=6 =>T  1==3 => F n=2      1
# n=2 2<=6 => T  2==3 => F n=3      2
# n=3 3<=6 => T  3==3 => T

# .......................................................
#  Continue
# n = 0
# while n <= 6:
#     n += 1
#     if n == 3:
#         continue
#     print(n)
# print("End")

#  Find the First Multiple of 7
# Skip Multiples of 3
#  Find the First Multiple of 7

# i = 1
# while i <= 4:
#     x = input("Enter a Number: ")
#     x = int(x)
#     if x % 7 == 0:
#         print("Found the First Multiple of 7!....")
#         break
#     i += 1

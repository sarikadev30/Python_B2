# n = len(arr) - 1
# revArr = arr[n::-1]
# if arr == revArr:
#     print("Pallindrome")
# else:
#     print("Not a Pallindrome")
# ............................................................................
# optimized approach
# arr = [1, 2, 4, 3, 2, 1]  # => 0 1 2 3 4 5
# l = 0  # 0
# r = len(arr) - 1  # 5
# ans = True
# while l <= r:
#     if arr[l] != arr[r]:
#         ans = False
#         break
#     l += 1
#     r -= 1

# # print(ans)
# if ans == True:
#     print("Pallindrome")
# else:
#     print("Not a Pallindrome")

# l= 0  r=5 ans=True  0<=5 => arr[0]=1 arr[5]=1 l=1 r=4
# l=1  r=4  ans=True  1<=4 => arr[1]=2 arr[4]=2 l=2 r=3
# l=2  r=3 ans=True 2<=3 => arr[2]=4 arr[3]=3  => ans=False
# ............................................................................
quantities = [2, 3, 5, 1]
quantities[len(quantities) - 1] = 89
prices = [50, 30, 20, 10]

print(quantities[0] * prices[0])
print(quantities[1] * prices[1])
print(quantities[2] * prices[2])
print(quantities[3] * prices[3])

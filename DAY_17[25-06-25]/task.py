stationary = []
stationary.extend(["pen", "pencil", "notebooks", "marker", "Eraser", "Sharpner"])
# print(stationary, len(stationary) - 1)

# print(stationary[len(stationary) - 1], len(stationary) - 1)
# print(stationary)
# stationary.remove("marker")
# print(stationary)
# stationary.pop(2)
# print(stationary)
# stationary.pop()          # no index => remove the last one
# print(stationary)


# movies = ["bahubali", "Spider-Man", "Iron Man", "Superman"]

# for i in range(len(movies)):
#     if i == 3:
#         break
#     print(movies[i])


# movies = ["bahubali", "Spider-Man", "Iron Man", "Superman", "Thor", "Avengers"]
# for i in range(len(movies)):
#     if i == 2 or i == 4:
#         continue
#     print(movies[i])


# arr = [45, 56, 89, 12, 100, 39]
# s = 0
# for i in arr:
#     s += i
# print(s, s / len(arr))


# Average of the elements of the list

# .........................................................................
# Revision
# a = [1, 2, 3, 4, 5,3,3,3,3]

# a.pop(3)
# print(a)
# a.remove(3)
# print(a)
# .........................................................................
# Inbuilt Functions
# arr = [45, 56, 89, 12, 100, 39]
# print(sum(arr))

# min() => smallest max() => largest

# print(min(arr), max(arr))

# arr = [45, 56, 89, 12, 100, 39]

# max1 = arr[0]
# min1 = arr[0]
# for i in range(1, len(arr)):
#     if arr[i] > max1:
#         max1 = arr[i]
#     if arr[i] < min1:
#         min1 = arr[i]


# print(max1, min1)

# max1=45

# i=1     56>45 => max1=56
# i=2     89>56 => max1=89
# i=3     12>89 =>
# i=4     100>89 => max1=100
# i=5     39>100 =>
# i=6
arr = [45, 56, 89, 12, 100, 39, 12, 12]
print(arr.index(12))

# Pallindrome
i = 0
j = len(arr) - 1
ans = True
while i <= j:
    if arr[i] != arr[j]:
        ans = False
        break
    i += 1
    j -= 1

print(ans)

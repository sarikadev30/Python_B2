# Data Types => primitive data types  => int float boolean string
# Non Primitive Data Types => List Tuple Set Dictionary

# x = 90  # => integer
# x=89
# x="Sam"
# a = [2, 4, 3, 3.0, True, "Sam"]

# Immutable
# s = "Sam"
# s[1] = "b"
# print(s[1])

# LIST => NON PRIMITIVE DATA TYPE

# a = [2, 3, 4, 5, 6, 7, 8]
# ab = [2, 4, 3, 3.0, True, "Sam"]
# .......................................................................
# Access the Elements of the List

# length of the list
# print(len(a))

# Positive Indexing => 0 - 6 (left to right)
# print(a[0], a[6], a[len(a) - 1])

# Negative Indexing  => (-1) - (right to left)
# print(a[-1])
# print(a[-4])

# ...................................................
# Slicing

# a = [2, 3, 4, 5, 6, 7, 8]
# ab = [2, 4, 3, 3.0, True, "Sam"]
# Syntax=>  a[start:end:step]
# ans = a[1:5:1]
# ans = a[1:5]
# ans = a[:5]
# ans = a[:5:2]

# ans = a[-1:-5:-1]
# ans = a[-1:-5:1]       # Empty List
# print(ans)

# K = [1, 2, 3, "Sam", "Danny", True, 3.4, [1, 4, 5, 6, 7]]
# left => right 0 right => left -1
# print(K[-1])
# print(K[4])
# print(K[-4])
# print(K[-1][2])   # 5
# print(K[-1][-3])    # 5

# print(type(K))


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(thislist[-4:-1])
# print(thislist[:4])
# print(thislist[2:5])
# print(thislist[2:])
# print(len(thislist))

# .............................................................................
# List Operations  => C=> Create R=> Read U=> Update D=> Delete
# a = [2, 3, 4, 5, 0, 67, 23, 12]

# Read particular element
# print(a[0])

# Read the whole list

# Looping over the index
# for i in range(len(a)):
#     print(i, a[i])

# Loop over the elements
# for j in a:
#     print(j)

# Update
# a = [2, 3, 4, 5, 0, 67, 23, 12]
# Replacing
# print(a[2])
# a[2] = 89
# print(a[2], a)

# for i in a:
#     i += 2
#     print(i)
# .....................................
# Addition
a = [2, 3, 4, 5, 0, 67, 23, 12]

# append => add at the end of the list
# a.append("Sam")
# print(a)
# insert => add at particular index
# a.insert(2, "Sam")
# print(a)
# extend => to add two or more list
# b = [3, 5, 6, 7, 9, 0]
# a.extend(b)
# b.extend(a)
# print(b)

# .....................................................
# Deletion
b = [3, 5, 6, 7, 9, 0, 7, 9, 3, 9]

# pop(index)   => empty => last index
# print(b.pop(2))
# b.pop(2)
# print(b)
# b.pop()
# print(b)


# remove(item)   => multiple occurances => remove first one
# b.remove(9)
# print(b)

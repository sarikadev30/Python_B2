"""
Count Frequency of Each Character
**Problem Statement:**
Write a function `char_frequency` that returns a dictionary containing the frequency of each character in the string.
print(char_frequency("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""

# def char_frequency(s):
#     d = {}
#     for i in s:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     return d
# print(char_frequency("misisipi"))

# d={}
# i=h => h in d => false else => d["h"]=1    d=>{"h":1}
# i=e => e in d => false else => d["e"]=1    d=> {"h":1,"e":1}
# i=l => l in d => false else => d["l"]=1    d=> {"h":1,"e":1,"l":1}
# i=l => l in d => true if=> d["l"]=d["l"]+1 d=> {"h":1"e":1,"l":2}
# i=o => o in d => false else => d["o"]=1    d=>{"h":1"e":1,"l":2,"o":1}

# ..............................................................................
"""
Flatten a Nested List**
**Problem Statement:**
Write a function called `flatten_list` that takes a list containing nested lists and 
returns a flat list with all the elements.
print(flatten_list([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]

"""
# x = [1, 2, 3, 4]
# # x.append([11, 12, 13, 14])
# x.append(1)
# x.extend([11, 12, 13, 14])
# print(x)
# x = [1, 2, 3, 4, 5]
# x = 0
# print(isinstance(x, list))


# def flatten_list(ls):
#     newLs = []
#     for i in ls:
#         if isinstance(i, list):

#             newLs.extend(flatten_list(i))
#         else:
#             newLs.append(i)
#     return newLs

# print(flatten_list([1, [2, [3, 4], 5], 6]))

# .....................................................................
# DRY RUN
# 1 =>  nl=>[1]
# [2,[3,4],5] => flatten_list([2,[3,4],5])
# 2        nl=>[1,2]
# [3,4] => flatten_list([3,4])
# 3    nl=>[1,2,3]
# 4    nl=>[1,2,3,4]
# 5        nl=>[1,2,3,4,5]

# 6  => nl=>[1,2,3,4,5,6]

# ....................................................................
# l1 =>[1,2,3] l2 => ["a","b","c"] => [1,"a",2,"b",3,"c"]
# l1=[1,2,3]
# l2=["a","b","c"]
# lmax=max(len(l1),len(l2))
# for i in range(lmax):
#     if i<len(l1):
#         print(i)
#     if i<len(l2):
#         print(i)


# [1,"a",2,"b"]
# ["a",1]

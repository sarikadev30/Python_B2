# CREATION OF TUPLE
# z = (1, 2, 3, 4, 5, 2, 3, 2, 3)
# x = tuple((1, 4, 2, 34, 12, 12, 23, 3, 4))
# print(z, x, type(x))

# print(x[8], z[-4])  # 4 2

# # Merging

# t = z + x
# print(t)

# # LOOPING
# for i in t:
#     print(i)

# for i in range(len(x)):
#     print(x[i])
# .................................................................
# Updation
#  convert tuple to list
#  update
#  list to tuple

# x = (1, 2, 3, 4, 5, 6, 7, 8, 1, 23, 56)
# # x[-2] = 123
# z = list(x)
# print(z, type(z), z[-2])
# z[-2] = 123
# print(z)
# x = tuple(z)
# print(x, type(x))

# ..............................................................................
# letters = set("mississippi")
# print(letters)
# print(len(letters))
# letters.pop()
# print(letters)

# print(letters.pop(), letters)
# # letters.pop()
# # print(letters)

# ..............................................................................
# DICTIONARY

# CRUD => CREATE READ UPDATE DELETE
# CREATE
# a = {"age": 23, "city": "New York", "name": "Sam", "name": "Danny"}
# x = dict({"apple": 1, "banana": 2, "kiwi": 3})
# Di = {1: "Hello", 2: "World"}
# # print(a, x, type(a), type(x))

# d = {
#     "name": ["Anny", "Bunny", "Danny", "Enav"],
#     "age": [25, 36, 22, 12],
#     "income": [90, 75, 80, 93],
#     # "name": "Sam",
# }

# READ
# print(a["name"])
# print(d["name"])
# print(x["apple"])
# print(Di[2])

# get function => to get the value using key
# print(d.get("age"))
# print(len(d.get("income")))
# print(d["name"][len(d["name"]) - 1])

# print(d["name"][len(d["name"]) - 1], "-", d["age"][len(d["name"]) - 1])

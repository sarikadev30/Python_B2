# DICTIONARY

# CRUD => CREATE READ UPDATE DELETE

# CREATE

# Problem 1 => Create a dictionary of student having keys => name age roll city
# ........................................................................................
d = {
    "name": ["Anny", "Bunny", "Danny", "Enav"],
    "age": [25, 36, 22, 12],
    "income": [90, 75, 80, 93],
}
# READ
# print(len(d.get("income")))
# print(d["name"][len(d["name"]) - 1])
# print(d["name"][len(d["name"]) - 1], "-", d["age"][len(d["name"]) - 1])

# Loop
# for i in d:
#     print(i, d[i])

# for i in range(len(d["name"])):

#     print(
#         f"Name: {d["name"][i]} - Age: {d["age"][i]} - Income (lakhs): {d['income'][i]}"
#     )

# Update
# a = {"name": "sam", "city": "Delhi", "age": 34}
# a["age"] = 23
# a["city"] = "NewYork"
# print(a)

# DELETE
# pop
# popItem
# del
# clear

# pop
# print(a.pop("age"))
# print(a)

# popItem
# print(a.popitem())
# print(a)

# del
# del a["city"]
# del d
# print(a, d)

# clear
# a.clear()
# print(a)

# get Method

# a = {"name": "sam", "city": "Delhi", "age": 34}
# print(a.get("roll", "Not Present"))

# keys
# print(a.keys())
# # values
# print(a.values())

# Loop
# for i in a.keys():
#     print(i, a[i])

# quantities = [2, 3, 5, 1]
# quantities[len(quantities) - 1] = 89
# x = "sam"
# print(x[1])
# x[1] = "o"
# print(x)

#  List is mutable and String is Immutable

# ...........................................................
# SETS   => Addition  Deletion  Search
# Creation of Set
# x = {4, 5, 6, 5, 6, 7, 8, 2, 3, 4, 5, 2, 3}
# print("Set x", x)

# y = {3, 5, 1, 2, 3}
# print(y, y.pop())

# Type Checking
# print(type(y))

# Searching
# print(4 in y, 4 in x)

# Addition
# y.add(78)
# print(y)

# Access the elements of set
# for i in y:
#     print(i)

# Another way to create set
# r = set((1, "Sam", "Danny", "Leo", 4, "Sam", "Danny"))
# print(r)
# print(r.pop())

# Deletion
# discard() => It do not raise error if value is not present
# remove() => It raise error if value is not present

# r.discard("Danny")
# r.remove("Danny")
# r.remove(89)
# r.discard(89)
# print(r)

# Add the list to the set
# x = [1, 2, 3, 4, 5, 6, 3, 1, 2]
# r.update(x)
# print(r)

# Clear all the elements or Make set Empty
# r.clear()
# print(r)

# list to set
# x = [1, 2, 3, 4, 5, 6, 3, 1, 2]
# y = set(x)
# print(y)

# set to list
# z = list(r)
# print(z)

# ..............................................................................
# Problem => Create a set for colors
#  Add blue to it and then print each element of the set
# ...............................................................................


# TUPLE
# CREATE => INDEXING => SLICING => MERGING

# CREATE
# z = (1, 2, 3, 4, "Sam", 4.4, True)
# print(z, type(z))

# print(z[1], z[-1])
# # z[3] = "Danny"              # Error
# print(z)
# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 14)
# print(t[3], t[3:6], type(t))
# 4        4
# 4,5,6       t[start:stop:step]     5
# tuple

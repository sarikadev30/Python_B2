# w+ mode => Write and Read

# with open("file.txt", "w+") as f:
#     f.write("Hi!..... Danny")
#     f.seek(0)
#     content = f.read()
#     print(content)

# with open("notes.txt", "w+") as f:
#     f.write("Hi I am a New File")

# ....................................................
# a+ mode  => Append and Read

# with open("file.txt", "a+") as f:
#     f.write("Joe...")
#     f.seek(0)
#     content = f.read()
#     print(content)

# ........... .........................................
# read() => read the whole file as a string
# readline() => read the line one by one
# readlines() => read the lines into a list

# with open("data.txt", "r+") as f:
#     content = f.readlines()
#     f.seek(0)
#     for i in content:
#         f.write(f"Hi!...{i}")

# ........................................................

# with open("data.txt", "r+") as f:
#     l = f.readlines()
#     print(l)
#     f.seek(0)
#     for i in range(len(l)):
#         f.write(f"Good Morning...{l[i]}")
#         if i == 4:
#             f.seek(0)
#             print(f.read())
#             break

# ............................................................
# Multi Dimensional List

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(x[0])
# print(y[0][0])
# print(y[0][1])
# print(len(x), len(y))

# for i in range(len(x)):
#     print(x[i])

# Sum of all the elements
# 1+2+3+4+5+6.....+12
for i in range(len(y)):
    for j in range(len(y[0])):
        print(y[i][j])


#
# items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# rows = len(items)
# cols = len(items[0])

# for i in range(rows):
#     for j in range(cols):
#         print(items[j][i], end="")

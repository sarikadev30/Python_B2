# Multi Dimensional List  => nested list

# each element of the mat => rows
# each rows particular index => columns
# mat1 = [[1, 2], [3, 4]]
# 2D List
# for i in range(len(mat1)):
#     for j in range(len(mat1)):
#         print(mat1[i][j])

# mat0 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# 4D list

# mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# 3*4 List
# print("rows :", len(mat))
# print("columns :", len(mat[0]))

# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         print(mat[i][j])

# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         print(mat[i][j], end=" ")

# ....................................................................
# Calculate Sum
# mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# # Calculate Sum for each row

# for i in range(len(mat)):
#     sum = 0
#     for j in range(len(mat[0])):
#         sum += mat[i][j]
#     print(sum)

# x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# 1 5 9 2 6 10 3 7 11 4 8 12

# for i in range(len(x[0])):
#     for j in range(len(x)):
#         print(x[j][i], end=" ")

# 0 => i => 0 1 2
# 1 => i => 0 1 2
# 2 => i => 0 1 2
# 3 => i => 0 1 2


# x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# 1 5 9 10 6 2 3 7 11 12 8 4


# x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# 1+2+3+4+5+8+9+10+11+12

# 00 01 02 03
# 10       13
# 20 21 22 23
# i==0 or i==len(x)-1 or j==0 or j==len(x[0])-1
# sum = 0
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         if i == 0 or i == len(x) - 1 or j == 0 or j == len(x[0]) - 1:
#             sum += x[i][j]
# print(sum)

# y = [[1, 2], [3, 4]]
# Left Diagonal
# 1  00
# 4  11

# Right Diagonal
# 2   01   => 1
# 3   10   => 1

# x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# 1   00
# 6   11
# 11  22
# 16  33

# Right Diagonal
# 4    03 => 3
# 7    12 => 3
# 10   21 => 3
# 13   30 => 3

# list = []
# listR = []
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         if i == j:
#             list.append(x[i][j])
#         elif i + j == len(x) - 1:
#             listR.append(x[i][j])

# print(list, listR)

# ....................................................

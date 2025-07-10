# d = {"a": 10, "b": 15, "c": 5, "d": 20}
# keyDel = []
# for key, val in d.items():
#     # print(key, val)
#     if val > 12:
#         keyDel.append(key)

# # print(keyDel)
# for i in keyDel:
#     del d[i]

# print(d)
# .................................................................
# Functions


# def fun():
#     print("Hello World!....")


# fun()
# for i in range(50):
#     fun()


def add(a, b):
    print(a + b)


# add(3, 5)

# Default Arguments


# def fun(z, y=1):
#     print(z * y)


# fun(4,3)
# fun(3)
# fun(4)

# ..................................
# Variable length Arguments

# def varFun(*t):
#     x = sum(t)
#     print(t, x)


# varFun(1, 2)
# varFun(1, 2, 5, 6, 6)
# varFun(1, 2, 6)


# ..................................
# keyworded Arguments

# def fun(name, age, city):
#     print(f"name: {name} , age : {age} , city : {city}")


# fun(city="Delhi", name="Sam", age=34)
# ......................................................


# def fun(z):
#     print(z)
#     x = sum(z)
#     avg = x / len(z)
#     print(x, avg)


# fun([1, 2, 3, 4, 5, 6, 7])
# fun([3, 4, 5])


# def fun(a, b):
#     print(a + b)


# fun(3, 4)
# fun(4, 5)

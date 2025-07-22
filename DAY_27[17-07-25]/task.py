# File Handling
# x = [1, 2, 3, 4, 5, 6, 7]
# avg = 23

# ......................................................
# 1st way: Our Responsibility to close it after the task completed
# file = open("file.txt", "r")
# print(file.read())

# file.close()

# .......................................................
# 2nd Way : File closes automatically

# with open("file.txt", "r") as f:
#     content = f.read()
#     print(content)

# ..........................................................
# File Modes => When opening files we need to specify the modes

# r => read mode
# ..........................................................
# w => write mode
# with open("file.txt", "w") as f:
#     f.write("Hi ! I am Sam..................")

# with open("notes.txt", "w") as f:
#     f.write("Hi ! I am Danny..................")
# ..........................................................
# a => append mode
# with open("notes.txt", "a") as f:
#     f.write("Hi ! I am a text file")

# ...........................................................
# Variants of Read and Write
# r+ => Read and Write
# w+ => Read and Write
# a+ => Read and Write

# r+ => Read and Then Write (NO FILE CREATION)
# with open("notes.txt", "r+") as f:
#     content = f.read()
#     print(content)
#     print(f.tell())
#     f.seek(12)
#     f.write("Bye")
# ...........................................................

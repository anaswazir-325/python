# file = open("file.txt","r")
# content = file.read()
# print(content)
# file.close()

# file = open("student.txt","r")
# read = file.read()
# print(read)
# file.close


# file = open("student.txt","w")
# file.write("my favourate book physics\n")
# file.write("my name is anas wazir\n")
# file.write("python in my DNA\n")
# file.write("my age 17 years old\n")
# file.close()

# file = open("student.txt","a")
# file.write("\ni am learning python")
# file.write("\nB/c python is my favourate")
# file.close




# file = open("file2.txt","x")
# file.close()

file = open("file2.txt","r+")
read = file.read()
print(read)

file.write("My name is anas khan\n")
file.write("i am 17 years old\n")
file.close()
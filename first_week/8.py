# F-string
name = "Anas wazir"
age = 17
print(f"my name is {name} and i am {age} year old. ")
print (f"next year i wil be {age + 1 } year old")

school_name = " Adil public school and college"
print(f"my school name is {school_name}.")

# format method
name = "Anas wazir"
age = 17.453
print("name: {}, age:{:.2f}".format(name,age))

# string input
name = input("Enter the name: ")
print("Name: ",{name})

# MULTIPLE inputs
x, y = input("Enter the two numbers separated by space: ").split()

x = int(x)
y = int(y)

print(f"Sum: {x + y}")

#  taking float input

price = float(input("Enter the price:"))
print(f"price with tax: {price * 1.1:.2f}")


# int method
num = input("Enter the first number:")
num2 = input("Enter the second number: ")
print("num: ",{num})
print("num2: ",{num2})

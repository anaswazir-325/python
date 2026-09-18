# try:
#     age = int(input("Enter your age:"))
# except ValueError:
#     print("Please enter your correct age")
# else:
#     print("Yes this your correct age")

try:
    number = int(input("Enter any number: "))
    if number % 2==0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input")
else:
    print("Correct")
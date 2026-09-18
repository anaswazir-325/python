# try:
#     filename = input("File name : ")
#     number = int(input("Enter the numer: "))
    
#     file = open(filename,"r")
#     read = file.read()
#     print(read)
#     file.close()
#     print(number)
# except ValueError:
#     print("invalid input")
# except FileNotFoundError:
#     print("Please correct your file name")
# else:
#     print("Yes correct")


# try:
#     number1 = int(input("Enter 1st number: "))
#     number2 = int(input("Enter 2nd number: "))
    
#     result = number1/number2
#     print(result)
# except(ValueError,ZeroDivisionError,TypeError) as e:
#     print(e)
    
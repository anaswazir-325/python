try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2
    print(result)
except(ValueError,ZeroDivisionError) as e:
    print(e)

finally:
    print("Finally is always executed, whether an exception occurs or not.")    
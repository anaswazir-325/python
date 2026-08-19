def add(a, b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    return a / b


while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exist")
    
    choice = input("Enter your choice: ")
    if choice == "5":
        print("Exist")
        break
    
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    
    if choice == "1":
        print(add(num1 , num2))
    elif choice == "2":
        print(subtract(num1 , num2))
    elif choice == "3":
        print(multiply(num1 , num2))
    elif choice == "4":
        print(divide(num1 , num2))
    else:
        print("Invalid choice")
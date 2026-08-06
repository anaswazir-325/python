# child, teenager, adult, or senoir
age = int(input("Enter the age: "))
 


if 1 <= age <= 12:
    print("You are a child")
    
elif 13 <= age <= 19:
    print("You are a teenager")
    
elif  20 <= age <= 64:
    print("You are a adult")
    
elif age >= 65:
    print("You are a senoir")
    
else:
    print("Error")
weight = int(input("Enter your weight: "))
Height = int(input("Enter your height: "))

BMI = weight / ( Height ** 2) 
if BMI < 18:
    catagory = "Under_weight"
elif BMI < 25:
    catagory = "Normal"
elif BMI < 30 :
    catagory ="Over_weight"
else:
    catagory = "Obese"
print(f"BMI: {BMI:.2f}")
print("Catagory",catagory)
         
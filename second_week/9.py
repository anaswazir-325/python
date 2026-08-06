# Voting Eligibility Checker
age = int (input("Enter your age: "))
citizen = input("Are you a cetizen yes/no: ")
if age >= 18 and citizen == "yes":
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")
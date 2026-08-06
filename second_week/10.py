# Simple Login System
Correct_username = "Anas"
Correct_passwered = "1234"

User_name = input("Username: ")
Passwered = input("Passwered: ")
if User_name == Correct_username and Passwered == Correct_passwered:
    print("Login successfull")
else:
    print("Invalid username or passwered")
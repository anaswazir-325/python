# dictionar = {
#     "name" : "Anas wazir",
#     "class" : "12th",
#     "from" : "wazir"
# }
# print(dictionar)

# nested dictionary
# student = {
#     "name" : "Anas wazir",
#     "subject" : {
#         "phy" : 90,
#         "che" : 95,
#         "com" : 99,
        
#     }
# }
# print(student)
# print(student["subject"])
# print(student["subject"]["che"])
# print(student["subject"]["phy"])
# print(student["subject"]["com"])













# info = {
#     "key" : "value",
#     # list in dictionary
#     "subject" : ["python", "Java", "C++"],
#     # Tuple in dicionary
#     "Today topic" : ("Dictionar" , "Set"),
#     "Name" : "Anas wazir",
#     "Learning" : "coding",
#     "Age" : 17,
#     "price" : 19.9,
#     "is_student" : True,
#     23 : "int",
#     19.8 : "price",
#     "True" : "Bolean",
# }
# nul_dictionary ={}
# # add any key in nul dictionary
# nul_dictionary["school"] = "Adil public high school"
# print(nul_dictionary)    
    
# # sign the key value
# info["Name"] = "Zahid Ullah"
# # add the key
# info["name"] = "Anas wazir"
# # print only topic today
# print(info["Today topic"])
# # print only subject
# print(info["subject"])
# # print All
# print(info)
# # print dictionary type
# print(type(info))












# Nested Dictionary
# school = {
#     "name " : "Adil public high school",
#     "student subject" : {
#         "phy" : 90,
#         "che" : 90,
#         "com" : 99,
#     }
    
# }

# school["total marks"] = (
#     school["student subject"]["phy"]
#      + school["student subject"]["che"]
#      + school["student subject"]["com"])

# school["Average"] = school["total marks"] / 3

# print("Physics: ",school["student subject"]["phy"])
# print("Chemistry: ",school["student subject"]["che"])
# print("Computer: ",school["student subject"]["com"])
# print("Total marks: ",school["total marks"])
# print("Average: ", school["Average"])
# print(school)










# i want in this dictionary to print all keys 
# student ={
#     "name" : "Anas khan",
#     "age" : 17,
#     "fathe name " : "Jameel khan"
# }
# The lenth of total keys
# print(len(student))
# print all keys
# print(student.keys())
# change in list
# print(list(student.keys()))
# In tuples
# print(tuple(student.keys()))













# i want this dictionary to print all value in this dictionary


# student = {
#     "name" : "Anas wazir",
#     "father name" : "Jameel khan",
#     "subject" : "computer science",
#     "i want to learn" : "python",
    
# }

# all values print
# print(student.values())

# value in list
# print(list(student.values()))

# value in tuple
# print(tuple(student.values()))

# lenth of the total value

# print(len(student))









# i want this dicionary to print items=> means pair (key:value)

# student_marks = {
#     "name" : "Anas wazir",
#     "phy" : 90,
#     "che" : 95,
#     "com" : 99,
        
# }


# print all item
# print(student_marks.items())

# convert dictionary to list
# print(list(student_marks.items()))

# convert dictionary to tuple
# print(tuple(student_marks.items()))

# length of all dictionary
# print(len(student_marks))








contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Phone")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter your choic: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Contact added!")

    elif choice == "2":
        name = input("Enter your name: ")

        if name in contacts:
            print(contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter your name: ")

        if name in contacts:
            phone = input("Enter your phone number: ")
            contacts[name]["phone"] = phone
            print("Phone updated!")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter your name: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found.")

    elif choice == "5":
        for name in contacts:
            print(name, contacts[name])

    elif choice == "6":
        break

    else:
        print("Invalid choice.")


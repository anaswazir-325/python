contact =  {}

while True:
    print("........CONTACT BOOK.........")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Show all contact")
    print("6. Exist")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        Email = input("Enter your email: ")
        
        contact[name] = {
            "Phone" : phone,
            "Email" : Email
        }
        print("Contact Added")
    elif choice == "2":
        name = input("Enter your name: ")
        if name in contact:
            print(name,contact[name])
        else:
            print("Contact not found")
    elif choice == "3":
        name = input("Enter your name: ")
        if name in contact:
            phone = input("Enter your phone number: ")
            contact[name]["phone"] = phone
            print("Update contact")
        else:
            print("contact not found")
    elif choice == "4":
         name = input("Enter your name: ")
         if name in contact:
             del contact[name]
             print("contact deleted")
         else:
             print("Contact not found")
    
    elif choice == "5":
        if contact:
            for name, details in contact.items():
                print(name, details)
        else:
            print("No contacts found")
             
    elif choice == "6":
             break
    else:
            print("Invalid choice") 
         
            
        
        

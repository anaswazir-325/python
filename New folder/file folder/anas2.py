# with open("file2.txt","r") as file:
#     read = file.read()
#     print(read)
    
# with open("file2.txt","r") as file:
#     read = file.readline()
#     print(read) 
    
    
    
# with open("file2.txt","r") as file:
#     for line in file:
#      print(line.strip())
     
# with open("file2.txt","r") as file:
#    print(file.tell())
#    file.read(5)
#    print(file.tell())
#    file.seek(5)



# with open("file4.csv","x") as file:
#     file.close()


# import csv
# with open("file4.csv","w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name","Marks"])
#     writer.writerow(["Anas wzir",95])
#     writer.writerow(["khan wali",95])
    
    
# import csv
# with open("file4.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# with open ("student_record.txt","x") as file:
#     file.close()


# with open("student_record.txt","w") as file:
#     name = input("Name : ")
#     marks = input("Marks : ")
#     file.write(name + " " + marks)
# print("Record Saved")
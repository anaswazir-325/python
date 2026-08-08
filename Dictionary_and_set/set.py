# numbers = {1,4,"anas wazir"}
# numbers.add("nabi") #add method on set
# print(type(numbers))
# set2 = set()
# print(type(set2))






# names = {"Anas wazir", "Zahid ullah", "Samad ullah"}
# names.remove("Anas wazir")
# print(type(names))
# print(names)




# student_name = set(input("Enter your name"))

# marks= {90 , 99 , 90}


# total_marks = 90 + 99 + 90
# average = total_marks / 3

# print(student_name)
# print(total_marks)
# print(average)

# mark = {}

# x = int(input("Enter the physics mark: "))
# mark.update({"Physics" : x})


# x = int(input("Enter the chemistry mark: "))
# mark.update({"chemistry" : x})


# x = int(input("Enter the coputer mark: "))
# mark.update({"computer" : x})

# total_marks = mark["Physics"] + mark["chemistry"] + mark["computer"]

# average = total_marks / 3



# print("Total marks: ",total_marks)
# print(f"Average: {average:.2f}")
# print(mark)





# course = {"chemistry", "physics", "biology"}
# Adding and removing element
# adding method
# course.add("computer")
# print(course)

# multiple value add to set
# course.update(["islamayat"],["cyber security"])
# print(course)

# remove item ; error if messing
# course.remove("chemistry")
# print(course)

# Removes item ; no error if messing
# course.discard("History")
# print(course)
# OR
# course.discard("cyber security")
# print(course)



# union set
# a = {1 , 2 , 4, 3}
# b = {1 , 2, 3, 4, 5, 6, 7, 8}
# print(a . union(b)) #remove automatically dublicate

# math_student = {"Anas wazir","zahid ullah", "nabi wazir"}
# phy_student = {"khan wali","saud","wasim"}
# print(math_student.union( phy_student))
# OR
# print(math_student|phy_student)

# Intersection set
# names = {"sara","billal","amir","anas"}
# names2 = {"anas","wasim","khan","sara"}
# print(names & names2)
# OR
# print(names.intersection(names2))






anas_course = {"physics", "computer", "chemistry"}
nabi_course = {"python","computer","javascript"}

common = anas_course & nabi_course
only_anas = anas_course - nabi_course
only_nabi = nabi_course - anas_course
all_courses = anas_course | nabi_course

print("Commen courses: ",common)
print("Only anas: ", only_anas)
print("Only nabi: ",only_nabi)
print("All courses: ",all_courses)
















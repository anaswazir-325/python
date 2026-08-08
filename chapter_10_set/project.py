student1 = set(input("Enter the student 1 courses: ").split())
student2 = set(input("Enter the student 2 courses: ").split())
student3 = set(input("Enter the student 3 courses: ").split())

# courses all three student share
commen_courses = student1 & student2 & student3

# courses unique to each student
unique_1 = student1 - (student2 | student3)
unique_2 = student2 - (student1 | student3)
unique_3 = student3 - (student1 | student2)


# full courses combined
all_courses = student1 | student2 | student3

print("Courses shared by all three students:")
print(commen_courses)

print("courses unique to student 1 ")
print(unique_1)

print("courses unique to student 2 ")
print(unique_2)


print("courses unique to student 3")
print(unique_3)

print("All courses combined")
print(all_courses)
# name = ["Anas khan", "zahidullah", "samad", "amir", "khan wali"]
# marks = [90,88,76,66,44]

# for i in range(5):
#     if marks[i] >= 90:
#         grade = "A"
#     elif marks[i] >= 80:
#         grade = "B"
#     elif marks[i] >= 70:
#         grade = "C"
#     elif marks[i] >= 60:
#         grade = "D"
#     else:
#         grade = "FAIL"
        
#     print(name[i], ":" ,marks[i] , "-" , grade)
# average = sum(marks)/5


# print("Class average: ", average)

# heighest = max(marks)
# heighest_index = marks.index(heighest)

# print("Heighest scorer: ",name[heighest_index])


# lowest = min(marks)
# lowest_indext = marks.index(lowest)
# print("Lowest scorer: ", name[lowest_indext])




















names = ["anas wazir", "samad ullah", "khan wali"]
marks = [90 , 55, 78]

for i in range(3):
    if marks[i] >= 90:
        grade = "A"
    elif marks[i] >= 70:
        grade = "B"
    elif marks[i] >= 60:
        grade = "C"
    else:
        grade = "FAIL"
        
    print(names[i], ":" , marks[i] , "-" , grade)


average = sum(marks) / 3

print("Average of this three student: ", average)

heighest = max(marks)

heighest_index = marks.index(heighest)

print("Heighest index: ", names[heighest_index])


lowest = min(marks)

lowest_index = marks.index(lowest)

print("Lowest index: ", names[lowest_index])




        
        
        
# Student Grade Calculator
mark = int(input("Enter the marks: "))

if mark >=90 :
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark >= 70:
    grade = "C"
else:
    grade = "Fail"
print("Grade:",grade)
    
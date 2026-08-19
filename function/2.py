# message = "I am global" # this is a global veriable becouse outside of function

# def name():
#     local_note = "I am local" # this is local veriable becouse inside of function
#     print(message)
#     print(local_note)
# name()



# name = "Anas wazir"

# def name_detail():
    
#     name2 = "Zahid Ullah"
#     print(name)
#     print(name2)
# name_detail()    
 
 
 
 
#  Recursive function
 
# def countdown(n):
#     if n == 0: # this is base case becouse the base case stop the function
#         print("Done!")
#         return
#     print(n)
#     countdown(n - 1) # this is recursive case
# countdown(5)    




# global keyword

# x = 10

# def number(num):
#     print(num)
#     global x 
#     x = 20
# number(x)
# print(x)    



# name = "Zahid Ullah"

# def name_detail(info):
#     print(info)
#     global name
#     name = "Anas wazir"
    
# name_detail(name)
# print(name)    




# number = (lambda x , x1: x + x1)
# print(number(3,5))

# num1 = (lambda n , n2 : n * n2)
# print(num1(4,8))

# num2 = (lambda y , y1 : y / y1)
# print(f"{num2(10,2):.2f}")

# name = (lambda name1 , name2: (name1 , name2))
# print(name("Anas wazir","Zahid Ullah"))

# total_marks = (lambda mark1 , mark2 , mark3: mark1 + mark2 + mark3)
# total = total_marks(90,99,95)
# print(total)
# average = (lambda x : x/3)
# print(average(total))



check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(29))

counter = 0

def increament():
    global counter
    counter += 67
increament()
increament()
print(counter)

add = lambda x , x1: x + x1
print(add(67,67))
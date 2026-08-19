# def calc_ave(a, b, c):
#     sum = a + b + c
#     ave = sum / 3
#     print(sum)
#     print(ave)
#     return sum, ave 
# calc_ave(90,99,98)

# print function
# print("anas", end=" ") #sep = " "
# print("wazir") #end = "\n"


# converter function

# def convert(usd_value):
#     pkr_value = usd_value * 277
#     print(usd_value,"USD =",pkr_value, "PKR")
# convert(10)   
   
# def converter(dhr_value):
#     pkr_value = dhr_value * 76
#     print(dhr_value ,"DHR =",pkr_value,"PKR")
# converter(40000)



# Defining and calling function
# def name(name):
#     print("Hello",name)
    
# name("Anas khan")



# paramater and argument
# def student_name(name): # (name) this is parametr
#     print(name)

# student_name("Anas wazir") # ("Anas khan") this is argument



# positional Argument
# def student_detail(name,age):
#     print("my name is ",name,"i am",age,"years old")
# student_detail("Anas khan",17) # matched by position ,name = "Anas khan",age = 17






# keyword argument
# def student_detail(name,age):
#      print("my name is ",name,"i am",age,"years old")
     
# student_detail(age=17,name="Anas khan") # order does not matter with keyword



# Default argument
# def student_detail(name,age = 20):
#      print("my name is ",name,"i am",age,"years old")
   
# student_detail(name = "Anas khan") #uses the default: anas 17 years old
# student_detail("zahid ullah", 17) # overrides by default


# *args
# def total(*args):
#      return sum(args) #(args) add multiple value
# print( total(5 , 7 , 100 ,6 ,7 ,8))
# print(total(10,9000,678,58769))


# **kwargs
# def student_info(**kwargs):
#      for key, value in kwargs.items():
#           print(f"{key} : {value}") # Here, kwargs automatically becomes the dictionary
# student_info(Name = "Anas wazir",age = 17, course = "Python")




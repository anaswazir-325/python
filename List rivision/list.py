# creating list
# name = ["anas","zahid","samad"]
# print(name)
# print(type(name))


# accessing list
# friuts = ["Apple","Bannana","Graph"]
# print(friuts[0])
# print(friuts[2])



# updating list item
# friuts = ["Anaas ", "Zahid","wasim"]
# friuts[0] = "amir"
# friuts[1] = "sadiq"
# print(friuts)



# Adding items
# num = [1 , 2, 3, 4]
# num.append(5)
# num.append(6)
# num.insert(2,"anas khan") # (index,"New value")
# num.insert(4,8)
# num.extend(["Apple","Bannana","Graph"])
# print(num)





# Removing items
# fruits = ["litchi","mango","orange","straberry"]
# fruits.remove("litchi") # specific index
# fruits.pop() # automatically last index remove
# fruits.clear() # Remove all item
# print(fruits)




# list slicing
# name = ["Anas khan","Sadiq","Samad Ullah","Zahid Ullah","wasim","Amir","Bilal"]
# print(name[1:])
# print(name[0:]) # all list item print
# print(name[:4]) # 0 to 4
# print(name[::-1]) # reverse 
# print(name[-4::-1])


# list operator
# num1 = [1, 2, 3, 4]
# num2 = [5, 6, 7, 8]
# print(num1 + num2) # conccatination
# print(num1 * 5) # repitition
# print(3 in num1)
# print(4 in num2)
# print(3 not in num2)

# copying list
# original = [1,2,3]
# copy = original.copy() # this a copy list
# original.append(4) # this a original list
# print(original)
# print(copy)

# sorting and reversing
# list = [1,4,3,5,2,6,7]
# list.sort() # Ascending
# print(list)
# list.sort(reverse=True) # Descending
# print(list)


# list comprehension
# squares = [x ** 2 for x in range(1,6)]
# print(squares)

# evens = [x for x in range(1,20) if x % 2==0]
# print(evens)


num = [56,78,90,99,3]
print(max(num))
print(min(num))
average = sum(num)/len(num)
print(average)





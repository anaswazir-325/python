# STRING indexing
# text = input("Enter any sentence: ")
# line_text = text[5]
# print(line_text)


# Negative indexing
# sentence = "Python"
# line_sentence = sentence[-1]
# print(line_sentence)

# string imutability
# text = "python"
# line_text = "J" + text[1:]
# print(line_text)

# string slicing
# word = "Anaskhan"
# print(word[0:4])
# print(word[:4])
# print(word[4:])
# print(word[::2])
# print(word[::-1])



# string concatanation and repitition
first = "Anas wazir"

second = "i like python"
third = first + " " + second
print(third)

# and repitition 
a = "ha"
print(a *3)

b = "Anas"
c = (b + ",") * 100
print(c)


# membership testing
sentence = "python is so easy"
print("java" in sentence)
print("python" in sentence)
print("python"not in sentence)
print("Java"not in sentence)


# string comparison
# print("banana"=="banana")
# print("Apple"=="Watermelon")
# # only check alpahebt 
# print("Anas"<"Banana")
# print("Apple"<"Banana")
# print("apple"<"Banana")
# print("Apple"<"banana")
# print("lichi">"Banana")



# common string method
# country = "afganistan"
# In Python, upper() changes all letters of a string into uppercase (capital letters).
# print(country.upper())
# In Python, lower() is a string method that converts all letters into lowercase (small letters).
# print(country.lower())
# first letter of every word into a capital letter
# print(country.title())
# In Python, capitalize() changes the first character of a string to uppercase and changes the remaining characters to lowercase.
# print(country.capitalize())




# Search method
# name = "my name is anas"
# print(name.find("is"))
# print(name.find("Wazir"))
# print(name.count("y"))
# print(name.startswith("my"))
# print(name.endswith("anas"))



# replace method
# text = "I like python"
# print(text.replace("python","khan"))
# print(text.replace("I like python","I am khan"))



# split and join
# sentence = "Python is easy to learn"
# print(sentence.split())
# sentence2 = "Anas,17,BScs"
# print(sentence2.split(","))
# join
# date = "_".join(["2026","07","30"])
# print(date)




# sentence = "    i am from waziristan "
# remove star and end space
# print(sentence.strip())
# only remove left space
# print(sentence.lstrip())
# only remove right space
# print(sentence.rstrip())





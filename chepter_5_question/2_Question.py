sentence = input("Enter the sentence: ")

vowel = "aeiou"
count = 0
for char in sentence .lower():
    if char in vowel:
        print(char,"This is a vowel")
        count += 1
    else:
        print (char,"The  is not a vowel")
print(count)        
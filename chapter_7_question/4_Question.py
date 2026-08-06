sentence = input("Enter the sentence: ")

vowel =[letter for letter in sentence if letter.lower() in "aeiou"]
print(vowel)
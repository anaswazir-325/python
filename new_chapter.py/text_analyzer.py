# sentence = "Python is very fun"


# # Word count
# word_count = len(sentence.split())
# reversed_sentence = sentence[::-1]



# # Vowel count
# vowel_count = 0

# for letter in sentence.lower():
#     if letter in "aeiou":
#         vowel_count += 1
  
    

# print(len(sentence)) 

# print("Word count:", word_count)
# print("Vowel count:", vowel_count)
# print(reversed_sentence)













sentence = input("Enter the sentence: ")

character = (len(sentence))
word_count = len(sentence.split())


vowel = 0
for letter in sentence.lower():
    if letter in "aeiou":
        vowel += 1
        
sentence_reversed = sentence[:: -1]       
print("Character: ",character)
print("Word count: ",word_count)
print("Vowel: ",vowel
      )
print("Reversed sentence: ",sentence_reversed)

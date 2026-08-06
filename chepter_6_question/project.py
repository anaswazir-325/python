
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

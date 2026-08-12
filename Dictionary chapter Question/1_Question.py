sentence = "The dog chased a cat"

word = sentence.split()

word_count = {}

for words in word:
    if words in word_count:
        word_count[words] += 1
    else:
        word_count[words] = 1
print(word_count)
        
    
# QUESTION: Get the length of every word in a list using map().

word = input("Enter a word to check the length:  ")
word_length = map(lambda x:len(x),word)
print(f'The length of your word is : {sum(list(word_length))}')  
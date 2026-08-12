# Reverse a string without using slicing ([::-1])


input1 =input("Enter your text top revserse the text : ")
sentence = ""
for char in input1:
     sentence = char + sentence
print(sentence)
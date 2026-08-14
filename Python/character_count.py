"""Take a sentence and:
count number of words
count number of characters (excluding spaces)"""

# WORD_COUNT
user_input = input("Enter your text here:- ")
words = (user_input.split())
print(f"Total words in this sentence is : {len(user_input.split())}")
# Char count
char =(user_input.replace(" ",""))
char_count = 0
for i in  char:
    char_count+=1
print(f"Total character in {user_input} is {char_count}")\

#Question ---->Find the first non-repeating character in a string
# Example: "aabbcde" → c
text = "aabccddeffgghyuj"
count = {}
for i in text:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
for i in text:
    if count[i] == 1:
        print(f"The first non-repeating character is: {i}")
        break  
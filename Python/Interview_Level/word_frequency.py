''' Word Frequency (String + Dictionary)

Input a sentence and print the frequency of each word.

Example: "python is fun python" → {'python': 2, 'is': 1, 'fun': 1}'''


text = "Python is fun python"
result = [x for x in text.split() ]
print(result)

text = "Python is fun python"
rslt = text.split()

for value ,i in enumerate(rslt):
    if i in rslt:
        count+=1 
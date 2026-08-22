# QUESTION :- From ["apple", "kiwi", "banana", "cat"], keep words with length greater than 4.


name = ["apple", "kiwi", "banana", "cat"]
result =filter(lambda x:len(x)>3,name)
print(f'Word length greater than 3 is : {list(result)}')


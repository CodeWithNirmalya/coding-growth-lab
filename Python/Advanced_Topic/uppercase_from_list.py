# QUESTION: Convert a list of names to uppercase using map().

choice = int(input("Enter how much name you wanna push in list: "))
new_list = []
for i in range(1,choice+1):
    name = (input("Enter the name to add in list: "))
    new_list.append(name)

uppercase_name = map(lambda x:x.upper(),new_list)
print(f'The given name from you in block letter is : {list(uppercase_name)}')
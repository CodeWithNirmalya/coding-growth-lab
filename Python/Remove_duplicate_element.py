'''Take a list and remove duplicate elements

Example:
[1,2,2,3,4,4] → [1,2,3,4]'''\
    
user_list = [1,2,2,3,4,4]

unique = set(user_list)
print(unique)

# WAY -02
user_list = [1,2,2,3,4,4]
value = set()
unique=[]
for i in user_list:
    if i not in value:
        unique.append(i)
        value.add(i)
print(unique)

# WAY -03

unq_item = list(dict.fromkeys(user_list))
print(unq_item)

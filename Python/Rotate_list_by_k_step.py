# QUESTION Rotate a list by k steps
'''Example:
[1,2,3,4,5], k=2 → [4,5,1,2,3]'''
my_list = [1,2,3,4,5]
key = int(input("Enter the number to rotate:- "))
new_list = my_list[:-key]
key_element = (my_list[-key:len(my_list)])
new_list.extend(key_element)
print(new_list)

my_list = [1, 2, 3, 4, 5]
k = int(input("Steps: "))

# The Magic Line:
k = k % len(my_list) # Handles keys larger than the list
result = my_list[-k:] + my_list[:-k]

print(result)
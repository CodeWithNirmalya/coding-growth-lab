'''
Flatten this list using list comprehension:

matrix = [[1,2], [3,4], [5,6]]
# Output: [1,2,3,4,5,6]'''

matrix = [[1,2], [3,4], [5,6]]

output = [item for sublist in matrix for item in sublist ]
print(f'Your flatten list is {output}')



# From a mixed list [1, "hi", 5, "python", 8], keep only integers using filter().

mixed_list = [1, "hi", 5, "python", 8]
result = filter(lambda x:type(x)==int,mixed_list)
print(f'Integers from your list are: {list(result)}')
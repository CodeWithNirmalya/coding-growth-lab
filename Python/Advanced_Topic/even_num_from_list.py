a = [1,3,4,25,12,77,58,42,15]

even_num = filter(lambda x:True if x% 2 ==0 else False,a)
print(f'The even number from the {a} is: {list(even_num)}')
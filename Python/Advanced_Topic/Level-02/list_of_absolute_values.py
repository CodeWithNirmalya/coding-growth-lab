nums = [10,-18,24,75,-78,-98,45,-24]
new_list = []
for i in nums:
    if i <0:
      new_list.append(i + (2 * -i) )
    else:
       new_list.append(i)
print(f'Absolute value using bruteforce method: {new_list}')



absolute_values = (map(lambda x:abs(x),nums))
print(f"Absolute value using map and abs function: {list(absolute_values)}")


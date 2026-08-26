# square = int(input("Enter a number to check the square: "))
# sqr_rslt = square**2
# num = int(input("Enter a number to to check highest power"))
# list1= []
# for i in range(num,sqr_rslt):
#     power = num**i
#     # print(power)
#     if power <square:
#         list1.append(2**i)
#         print(list1)  
#         # print (f'This is the power value of {num} ** {i} = {list1}')

# print(f'The Highest power value of {num} ** {i} = {list1}')






limit = int(input("Enter the limit: "))
base = int(input("Enter the base number: "))

power = 0

while base ** power < limit:
    power += 1

power -= 1

print(f"Highest power is {base}^{power} = {base ** power}")


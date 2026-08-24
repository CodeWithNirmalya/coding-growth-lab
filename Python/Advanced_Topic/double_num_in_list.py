# QUESTION: Double every number in a list using map() + lambda.

choice = int(input("Enter how much element you wanna push in list: "))
new_list = []
for i in range(1,choice+1):
    num = int(input("Enter the number to add in list: "))
    new_list.append(num)

double = map(lambda x:x*2,new_list)
print(f'The double of each number from the given list is: {list(double)}')


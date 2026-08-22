# QUESTION:- From a list of numbers, keep only numbers greater than 50 using filter().
choice = int(input("Enter how much element you wanna push in list: "))
new_list = []
for i in range(1,choice+1):
    num = int(input("Enter the number to add in list: "))
    new_list.append(num)

above50 = filter(lambda x:x>50,new_list)
print(f'This number is greater than 50 from your given list: {list(above50)}')
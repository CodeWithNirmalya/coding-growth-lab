# Take two lists from the user (same length). Print the greater value between those.    
list_one = []
list_two = []
choice = int(input("Enter how much number you wanna add in both list: "))
for i in range(choice):
    num = int(input("Enter the nunbers for the first list: "))
    list_one.append(num)
print(f'This is the first list: {list_one}')

for i in range(choice):
    num2 = int(input("Enter the nunbers for the second list: "))
    list_two.append(num2)
print(f'This is the second list: {list_two}')


if (sum(list_one))>(sum(list_two)):
    print(f'This is the list with highest value: {list_one}')    
elif (sum(list_one))==(sum(list_two)):
    print(":-:> Both list has same value as per sum of those values")
else:
    print(f'This is the list with highest value: {list_two}')



# Take two lists from the user (same length). Print the greater value at each index. 
print(":-:> Greater value at each index:")

for i in range(choice):
    if list_one[i]>list_two[i]:
        print(list_one[i],end = " ")
    else:
        print(list_two[i],end = " ")
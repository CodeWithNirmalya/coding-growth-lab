count = int(input("How much element you wanna add in the list: "))
num_list = []
for i in range(1,count+1):
    num = int(input("Enter the value: "))
    num_list.append(num)

res = [(i,i*i) for i in num_list]
print(f'The original numbers and square are : {res}')
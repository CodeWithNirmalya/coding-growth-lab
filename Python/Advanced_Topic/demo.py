choice = int(input("Enter how much element you wanna push in list: "))
new_list = []
for i in range(1,choice+1):
    num = int(input("Enter the number to add in list: "))
    new_list.append(num)




a = [10,20,30,40,50]
square = [i**2 for i in range(a)]
print(square)





a = [1,3,4,25,12,77,58,42,15]
even_num = map(lambda x:x%2==0,a)
print(list(even_num))
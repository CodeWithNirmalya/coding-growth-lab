with open('demo_file.txt','r') as f:
    data = f.read().lower().split()

choice = input("Please enter the word you wanna count: ").lower()
#Brute_force ---->
count= 0
for i in data:
    if i == choice:
        count +=1
print(f'"{choice}" is present {count} times')


#using Built-in Method!!
word_count = data.count(choice)
print(word_count)
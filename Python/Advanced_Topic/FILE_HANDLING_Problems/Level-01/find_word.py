with open('demo_file.txt','r') as f:
    words = f.read().lower().split()
   

choice = input("Please enter a word to check its present or not: ").lower()


# if choice in words:
#     print(f"{choice} is found in your file")
# else:
#     print(f'{choice} is not found in your file')

result = 'found' if choice in words else 'not found'
print(f'"{choice}" was {result} in the file.')
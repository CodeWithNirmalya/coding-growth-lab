'''
QUESSTION: Read a File

Read and print the entire file.

Then print it line by line.'''


#Read the entire file
try:
    with open("demo_file.txt",'r') as f:
        context = f.read()
        print(f'The whole Context from your file is: {context}')
except FileNotFoundError as err:
    print(f"You got an error while run this program: {err}")
finally:
    print("\nFile reading operation completed.")


# Print line by line

try:
    with open('demo_file.txt','r') as frd:
     for i,line in enumerate(frd,start= 1):
        print(f'Line: {i}  {line.strip()}')
except FileNotFoundError as err:
    print(f"You got an error while run this program: {err}")
finally:
    print("\nFile reading operation completed.")
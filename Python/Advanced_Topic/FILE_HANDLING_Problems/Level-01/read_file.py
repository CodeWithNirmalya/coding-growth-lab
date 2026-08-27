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



# Modern Pytonic Way
try:
    with open("demo_file.txt", "r") as f:
        # Read entire file
        content = f.read()
        print("Whole file:")
        print(content)

    with open("demo_file.txt", "r") as f:
        # Read line by line
        print("\nLine by line:")
        for i, line in enumerate(f, start=1):
            print(f"Line {i}: {line.strip()}")

except FileNotFoundError as err:
    print(f"Error: {err}")

finally:
    print("File reading operation completed.")

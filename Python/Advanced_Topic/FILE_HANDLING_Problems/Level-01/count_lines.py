# Question : Count Lines
#Count total number of lines in a files

try:
    with open('demo_file.txt','r') as f:
        for i, line  in enumerate(f,start = 1):
            print(f'Line_no: {i} {line.strip()})')
except FileNotFoundError as err:
    print(f"You got an error...{err}")

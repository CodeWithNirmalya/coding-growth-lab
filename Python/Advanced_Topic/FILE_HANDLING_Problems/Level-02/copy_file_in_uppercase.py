'''Uppercase File
Read a file and create another file where everything is uppercase.'''


with open('demo_file.txt','r') as f:
    data = f.read().upper()
with open('copied_text.txt','w') as fc:
    fc.write(data)
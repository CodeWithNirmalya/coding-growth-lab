# QUESTION: Copy File
#Copy contents of source.txt to backup.txt.

with open('demo_file.txt','r') as f:
    data = f.read()
with open('backup.txt','a') as fc:
    fc.write(data)
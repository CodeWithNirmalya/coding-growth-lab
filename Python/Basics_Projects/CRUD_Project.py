from pathlib import Path
import os

def fileandfolder():
    path = Path('')
    items = path.rglob("*")
    for i,item in enumerate(items):
        print(f'{i+1} : {item}')
print("Your file list in this system are below: ")
fileandfolder()

#Create Folder Function
def createfile():
    try:
        fileandfolder()
        name = input("PLease enter your name of the file: ")
        p= Path(name)   
        if not p.exists() and  p.is_file():
            with open(p,'w') as f:
                data = input("What you want to write inside the file: ")
                f.write(data)

            print("File created succesfully")
        else:
            print("This file is already exist in system")
    except Exception as err:
        print(f"You have got an error {err}")

# User can see the content of the file 
def readfile():
    try:
        fileandfolder()
        name = input("Enter the file of your name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as f:
                data = f.read()
                print(data)
            print("Readed Successfully")
        else:
            print(f'{name} - this file is not exist')
    except Exception as err:
        print(f"You have got an unexpected error: {err}")
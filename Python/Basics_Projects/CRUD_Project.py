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
        if not p.exists():
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


def updatefile():
    try: 
        fileandfolder()
        name =input("Enter the name of your file: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 to change the name of your file: ")
            print("Press 2 to rewrite the content of your file: ")
            print("Press 3 to add some content in your file")

            ans = int(input("Enter the choice from the above menu: "))

            if ans ==1:
                filename = input("Please enter the new name of your file: ")
                p2 = Path(filename)
                p.rename(p2)

            elif ans ==2:
                with open(p,'w') as f:
                    data = input("Please enter the data for replace your old data: ")
                    f.write(data)
                print("The new data are succesfully replace your old data")
            elif ans ==3:
                with open(p,'a') as f:
                    data = input("Please enter the data you wanna add in your file: ")
                    f.write(" "+data)
                print("New Data are added with your old content")
            else:
                print("Invalid output")
        else:
            print("File is not exist")
    except Exception as err:
        print(f"You have got an error {err}")


def deletefile():
    try:
        fileandfolder()
        name = input("PLease enter the name of your file to delete : ")
        p= Path(name)
        if p.exists() and  p.is_file():
            os.remove(p)
            print("The file is deleted succesfully...!")
        else:
            print(f"{name} is not exist in the system")
    except Exception as err:
        print(f"You have got an error {err}")


print("Press 1 to create a new file")
print("Press 2 to read your file")
print("Press 3 to update your file")
print("Press 4 to delete your file")
ans = int(input("Enter your choice here to perform the tasks: "))

if ans ==1:
    createfile()
elif ans ==2:
    readfile()

elif ans ==3:
    updatefile()
elif ans ==4:
    deletefile()
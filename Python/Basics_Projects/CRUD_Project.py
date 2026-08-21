from pathlib import Path
import os

def fileandfolder():
    path = Path('')
    items = path.rglob("*")
    for i,item in enumerate(items):
        print(f'{i+1} : {item}')
print("Your file list in this system are below: ")
fileandfolder()
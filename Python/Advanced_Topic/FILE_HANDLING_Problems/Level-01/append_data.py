'''
QUESTION : Append Data
           Ask the user for a new line.
           Append it to notes.txt.
'''

# with open('demo_file.txt','a') as f:
#     f.write("\nHey I added a line ...!!")


data = input("please enter your desired content to add in your file...")

try:
    choice = int(input("Do you wanna add your content in next line? if yes press 1 otherwise 0: "))
    with open("demo_file.txt" ,'a') as f:
         if choice == 1:
                f.write('\n' + data)
         else:
            f.write(data)
            
except ValueError :
    print("Please check your input...",ValueError)
except Exception as err:
    print(f"You got an error:- {err}")
finally:
    ("Thank you!!")

#Print updated file ... 
with open("demo_file.txt", "r") as f:
    print(f.read())


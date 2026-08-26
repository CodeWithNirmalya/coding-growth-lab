# Create a multiplication table of 7 (1–10) using list comprehension.

# mltplctn_tbl =[7*x for x in range(1,11)] 

#The multiplication table of 7
table = [f"7 × {i} = {7*i}" for i in range(1, 11)]

print(f'The multiplication table of 7 is: {table}')

# The Multiplication Table of user choice:
num = int(input("Enter the number you wanna calculate multiplication table: "))

mltplctn_tbl = [f'{num} X {i} = {num*i}' for i in range(1,11)]
print(mltplctn_tbl)



# USING a FUNCTION
def multiplication_table(num):
    return [f"{num} × {i} = {num*i}" for i in range(1, 11)]

print(*multiplication_table(7), sep="\n")

num = int(input("\nEnter a number: "))
print(*multiplication_table(num), sep="\n")
# QUESTION:- Create a list of cubes of only odd numbers from 1–20 using list comprehension.

cube = [i**3 for i in range (1,21) if i %2!=0]
print(f'The cube of all odd number between 20 is {cube}')

'''Example:
listen & silent → True'''
a = input("Enter first text to check anagarm:- ").lower()
b = input("Enter Sec0nd text to check anagarm:-").lower()
print(f"{a} and {b} ARE anagrams") if sorted(a) == sorted(b) else print(f"{a} and {b} are NOT anagrams")chat
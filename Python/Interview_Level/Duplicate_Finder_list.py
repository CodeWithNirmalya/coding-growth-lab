# # Input a list and print only the duplicate elements (without repeating duplicates).
# # Example: [1,2,3,2,4,1,5] → [1,2]

# # Bruteforce Technique
# my_lst = [1,2,3,2,4,1,5]
# unique = []
# repeted = []
# for i in my_lst:
#     if i not in unique:
#         unique.append(i)
#     else:
#         repeted.append(i)
# print(unique)
# print(repeted)


# Using List Comprehension
list_one = [1,2,3,2,4,1,5]
duplicates = [i for i in list_one if list_one.count(i) > 1]
print(list(duplicates))







my_lst = [1,2,3,2,4,1,5]

seen = set()
duplicates = []

for i in my_lst:
    if i in seen:
        if i not in duplicates:
            duplicates.append(i)
    else:
        seen.add(i)

print(duplicates)




from collections import Counter

my_lst = [1,2,3,2,4,1,5]

count = Counter(my_lst)

duplicates = [key for key, value in count.items() if value > 1]

print(duplicates)
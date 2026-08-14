"""Find missing number from list
Example:
[1,2,3,5] → 4"""
list1 = [1,2,3,5]
print(list1[-1])
list_sum = (sum(list1))
excepted_sum = 0
for i in range(1,6):
    excepted_sum +=i
print(sum)
print(f"Missing  number in this list is :-{excepted_sum-list_sum}")

"""Find all pairs in list whose sum = target
Example:
[1,2,3,4], target=5 → (1,4), (2,3)"""

list1 = [1,2,3,4]
sum = 0
target =5
for i in list1:
   for j in list1:
       if j ==i:
           continue
       else:
           sum = i+j
           if sum == target:
               print(f"final combination which can be sum of 5: -{i,j}")
# better way
list1 = [1, 2, 3, 4]
target = 5
seen = set()

for num in list1:
    needed = target - num
    if needed in seen:
        print(f"Found pair: ({needed}, {num})")
    seen.add(num)
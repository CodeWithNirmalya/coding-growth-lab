"""Move all zeros to end
Example:
[0,1,0,3,12] → [1,3,12,0,0]"""
list1 = [0,1,0,3,12]
non_zero = []
zero = []
for i in list1:
    if i == 0:
       zero.append(i)
    else:
        non_zero.append(i)
print(non_zero + zero)

# BEST WAY TO SOLVE!!list1 = [0, 1, 0, 3, 12]
# We sort by checking: "Is this number zero?" 
# This pushes "True" (zeros) to the back.
list1.sort(key=lambda x: x == 0)
print(list1)
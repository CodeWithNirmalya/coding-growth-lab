arr = list(map(int, input("Enter numbers: ").split()))

# 'seen' keeps track of numbers we have already encountered
seen = set()

# 'duplicates' stores numbers that appear more than once
duplicates = set()

for num in arr:

    if num in seen:
        # We have already seen this number,
        # so it is a duplicate
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate elements:", list(duplicates))
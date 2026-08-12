arr = list(map(int, input("Enter numbers: ").split()))

# Initially assume the first element is the largest
largest = arr[0]

for num in arr:
    # If we find a bigger number, update largest
    if num > largest:
        largest = num

print("Largest:", largest)
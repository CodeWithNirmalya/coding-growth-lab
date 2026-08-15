s = input("Enter a string: ")

# Dictionary will store character as key and its count as value
frequency = {}

for ch in s:
    # If character already exists, increase its count
    # Otherwise, start its count from 1
    frequency[ch] = frequency.get(ch, 0) + 1

print(f"here the frequency of the code {frequency}")
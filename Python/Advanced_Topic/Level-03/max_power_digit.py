






limit = int(input("Enter the limit: "))
base = int(input("Enter the base number: "))

power = 0

while base ** power < limit:
    power += 1

power -= 1

print(f"Highest power is {base}^{power} = {base ** power}")

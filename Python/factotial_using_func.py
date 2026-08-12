# Question ---Find factorial of a number using function
def factorial(n):
    # Initialize factorial result to 1
    fact = 1
    # Iterate from 1 to n (inclusive) to multiply all numbers
    for i in range(1,n+1):
        # Multiply fact by each number in the range
        fact*=i
    # Display the factorial result
    print(f"The factorial of {n} is {fact}")

# Take user input and calculate factorial
factorial(int(input("Enter the number: ")))
# Question ---Find factorial of a number using function
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(f"The factorial of {n} is {fact}")

factorial(int(input("Enter the number: ")))
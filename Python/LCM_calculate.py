# LCM OF TWO NUMBERS
import math
num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))
lcm = num1*num2/(math.gcd(num1,num2))
print(int(lcm))
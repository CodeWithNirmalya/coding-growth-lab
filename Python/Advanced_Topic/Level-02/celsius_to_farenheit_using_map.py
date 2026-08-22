# QUESTION:- Convert Celsius list [0, 20, 37, 100] to Fahrenheit using map() + lambda.
cel_temp = [0, 20, 37, 100]

faren_temp = map(lambda x:(x*1.8)+32,cel_temp)

''' use can also  use this standard formula
faren_temp = list(map(lambda c: (c * 9/5) + 32, cel_temp))'''

print(list(faren_temp))
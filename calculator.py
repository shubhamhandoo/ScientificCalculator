def square_root(x):
    if x < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return x ** 0.5

def factorial(x):
    if x < 0:
        return "Error: Factorial is not defined for negative numbers."
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

def natural_log(x):
    if x <= 0:
        return "Error: Natural logarithm is only defined for positive numbers."
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

def power(x, b):
    result = 1
    for _ in range(int(abs(b))):
        result *= x
    if b < 0:
        result = 1 / result
    return result
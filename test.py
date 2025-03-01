import calculator

def test_calculator():
    assert calculator.square_root(4) == 2.0
    assert calculator.square_root(-1) == "Error: Cannot calculate the square root of a negative number."
    assert calculator.factorial(5) == 120
    assert calculator.factorial(-3) == "Error: Factorial is not defined for negative numbers."
    assert round(calculator.natural_log(2), 5) == round(1000.0 * ((2 ** (1/1000.0)) - 1), 5)
    assert calculator.natural_log(0) == "Error: Natural logarithm is only defined for positive numbers."
    assert calculator.power(2, 3) == 8
    assert calculator.power(2, -3) == 0.125
    print("All test cases passed!")

if __name__ == "__main__":
    test_calculator()
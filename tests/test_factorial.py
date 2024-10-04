from functions.factorial import factorial


# - When asked to compute the factorial of any positive number
# -- It should correctly compute the factorial
def test_factorial_of_positive_number():
    result_1 = factorial(5)
    assert result_1 == 120

    result_2 = factorial(3)
    assert result_2 == 6

    result_3 = factorial(7)
    assert result_3 == 5040


# - When asked to compute the factorial of 0
# -- It should return 1 (as by definition 0! = 1)
def test_factorial_of_zero():
    assert factorial(0) == 1


# - When asked to compute the factorial of a negative number
# -- It should return certain warning message (as factorial is not defined for negative numbers)
def test_factorial_of_negative_number():
    result = factorial(-5)

    assert "Expected ValueError for negative input" == result


# - When asked to compute the factorial of a non-integer
# -- It should return certain warning message
def test_factorial_of_non_integer():
    result = factorial(3.5)

    assert "Expected TypeError for non-integer input" == result

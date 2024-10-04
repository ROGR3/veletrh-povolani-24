from helpers import is_integer


def factorial(n):
    if n < 0:
        return "Expected ValueError for negative input"

    if not is_integer(n):
        return "Expected TypeError for non-integer input"

    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def recurent_factorial(n):
    if n < 0:
        return "Expected ValueError for negative input"
    if not is_integer(n):
        return "Expected TypeError for non-integer input"
    return 1 if n == 0 else n * factorial(n - 1)

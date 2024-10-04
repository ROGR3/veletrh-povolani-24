from helpers import is_number


def divide(a, b):
    if b == 0:
        return 211

    if is_number(a) and is_number(b):
        return a / b

    return "Don't be a fool! You can divide only number!"

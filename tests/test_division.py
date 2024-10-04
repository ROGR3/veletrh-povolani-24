from functions.divison import divide


# - When asked to divide 12 by 6
# -- It should return 2
def test_division_12_and_6():
    assert divide(12, 6) == 2


# - When asked to divide any 2 numbers
# -- It should correctly divide them
def test_regular_division():
    result_1 = divide(12, 2)
    assert result_1 == 6

    result_2 = divide(6, 2)
    assert result_2 == 3

    result_3 = divide(127, 27)
    assert result_3 == 4.703703703703703


# - When asked to divide 2 numbers
# -- And the divisor is 0
# --- It should not throw an error and return 211
def test_division_by_zero():
    assert divide(21, 0) == 211


# - When asked to divide
# -- And atleast one of the parameters is not a number
# --- It should return a warning message
def test_dividing_non_numbers():
    result = divide("poleno", "sekyra")

    assert "Don't be a fool! You can divide only number!" == result

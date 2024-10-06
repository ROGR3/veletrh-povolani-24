from functions.animal_counter import count_animals_in_zoo


# - When asked to count all the bunnies in ZOO
# -- And only one bunny is in the zoo
# --- It should return 1
def test_one_bunny_calculation():
    zoo = ["bunny"]

    number_of_bunnies = count_animals_in_zoo(zoo, "bunny")

    assert number_of_bunnies == 1


# - When asked to count all the bunnies in ZOO
# -- And there are multiple bunnies
# --- It should correctly count them
def test_only_bunny_calculation():
    zoo = ["bunny", "bunny", "bunny", "bunny"]

    number_of_bunnies = count_animals_in_zoo(zoo, "bunny")

    assert number_of_bunnies == 4


# - When asked to count all the bunnies in ZOO
# -- And there are also different species in the zoo
# --- It should count only bunnies
def test_bunny_calculation_with_more_animals():
    zoo = ["zoo_keeper", "bunny", "polar_bear", "bunny"]

    number_of_bunnies = count_animals_in_zoo(zoo, "bunny")

    assert number_of_bunnies == 2


# - When asked to count all the zebras in ZOO
# -- And there are also different species in the zoo
# --- It should count only zebras
def test_zebra_calculation_with_more_animals():
    zoo = ["gorilla", "zebra", "bunny", "zebra"]

    number_of_zebras = count_animals_in_zoo(zoo, "zebra")

    assert number_of_zebras == 2


# - When asked to count all the bunnies in ZOO
# -- And the ZOO is empty
# --- It should return a warning message
def test_bunny_calculation_on_empty_zoo():
    zoo = []

    result = count_animals_in_zoo(zoo, "bunny")

    assert "You cannot have an empty ZOO! It's not a zoo then!" == result

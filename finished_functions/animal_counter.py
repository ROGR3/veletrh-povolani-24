def count_animals_in_zoo(zoo, serached_animal):
    if zoo:
        return len([animal for animal in zoo if animal == serached_animal])

    return "You cannot have an empty ZOO! It's not a ZOO then!"

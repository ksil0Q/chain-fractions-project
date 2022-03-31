import random

result = []


def make_fraction(floors, maximum_value) -> float:
    value = random.randint(1, maximum_value)
    if floors != 0:
        return value + 1 / make_fraction(floors - 1, maximum_value)
    return 10


def main(number_of_fractions, number_of_floors, maximum_value):
    for i in range(number_of_fractions):
        fraction = 0 + 1/make_fraction(number_of_floors - 1, maximum_value)
        result.append(fraction)
    return result

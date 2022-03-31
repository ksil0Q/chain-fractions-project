import random
import numpy as np


def make_fraction(floors, maximum_value) -> float:
    value = random.randint(1, maximum_value)
    if floors != 0:
        return value + 1 / make_fraction(floors - 1, maximum_value)
    return 10


def main(number_of_fractions, number_of_floors, maximum_value):
    result_dict = {round(x, 3): 0 for x in np.arange(0, 1.05, 0.01)}
    for i in range(number_of_fractions):
        fraction = 0 + 1/make_fraction(number_of_floors - 1, maximum_value)
        fraction = round((fraction // 0.01) * 0.01, 5)
        result_dict[fraction] += 1

    return result_dict

"""Some utilities"""
import math
import random


MU = 0
SIGMA = 1
NORMAL_DISTRIBUTION_RANGE = 3


class KanError(Exception):
    pass
    # def __init__(self, message):
    #    Exception.__init__(message)
    #     self.message = message

    # def __str__(self):
    #    return str(self.message)


def normal_distribution(x: float, mu: float, sigma: float) -> float:
    return math.exp(-((x - mu)**2) / (2 * (sigma**2))) \
           / (sigma * math.sqrt(2*math.pi))


def get_proportion_with_normal_distribution(
        mu: float = MU,
        sigma: float = SIGMA,
        range_x: float = NORMAL_DISTRIBUTION_RANGE
    ) -> float:
    while True:
        proportion = random.random()
        x = proportion * range_x
        probability = normal_distribution(x, mu, sigma)
        if random.random() < probability:
            return proportion

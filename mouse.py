"""Encapsulate pyautogui's mouse operations"""
# import pyautogui
import random
# import time
import math
import utils
# from matplotlib import pyplot


def get_random_point_in_circle_with_normal_distribution(
        x, y, radius, mu=utils.MU, sigma=utils.SIGMA,
        range_x=utils.NORMAL_DISTRIBUTION_RANGE):
    radian = math.pi * 2 * random.random()
    new_radius = radius * utils.get_proportion_with_normal_distribution(
        mu, sigma, range_x)
    x = x + new_radius * math.cos(radian)
    y = y + new_radius * math.sin(radian)
    return round(x), round(y)


def test_get_random_point_in_circle():
    x_, y_ = [], []
    for i in range(1000):
        x, y = get_random_point_in_circle_with_normal_distribution(0, 0, 100)
        x_.append(x)
        y_.append(y)

    pyplot.scatter(x_, y_, alpha=0.6, s=2)
    pyplot.show()


def get_random_point_in_rectangle_with_normal_distribution(
        x, y, radius_x, radius_y,
        mu=utils.MU, sigma=utils.SIGMA,
        range_x=utils.NORMAL_DISTRIBUTION_RANGE):
    proportion = \
        utils.get_proportion_with_normal_distribution(mu, sigma, range_x)
    radius_x *= proportion
    proportion = \
        utils.get_proportion_with_normal_distribution(mu, sigma, range_x)
    radius_y *= proportion
    x = x + random.choice([-1, 1]) * radius_x
    y = y + random.choice([-1, 1]) * radius_y
    return round(x), round(y)


def test_get_random_point_in_rectangle():
    x_, y_ = [], []
    for i in range(5000):
        x, y = get_random_point_in_rectangle_with_normal_distribution(
            0, 0, 200, 100)
        x_.append(x)
        y_.append(y)

    pyplot.scatter(x_, y_, alpha=0.6, s=1)
    pyplot.show()


def test():
    """Do some test"""
    # test_get_random_point_in_circle()
    test_get_random_point_in_rectangle()


def main():
    """Main process"""
    test()


if __name__ == '__main__':
    main()

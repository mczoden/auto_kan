"""Simulate human mouse behavior"""
import random
import math
import time

import pyautogui
import utils
from utils import KanError
import mouse

from game_gui import Area, Shape


POINT_JITTER_PIXEL = 5


def debug(message: str):
    print('[{} Human Mouse] {}'.format(
        time.strftime("%m-%d %H:%M:%S", time.localtime()),
        message))


def point_jitter(x: int, y: int, pixel: int = POINT_JITTER_PIXEL):
    if pixel == 0:
        return x, y
    if pixel < 0:
        pixel = -pixel
    pixel = int(pixel)
    x += random.choice(range(-pixel, pixel + 1))
    y += random.choice(range(-pixel, pixel + 1))

    return x, y


def get_random_point_in_circle(
        x: int,
        y: int,
        radius: float,
        jitter_pixel: int = 15,
        mu: float = utils.MU,
        sigma: float = 1.75,
        range_x: int = utils.NORMAL_DISTRIBUTION_RANGE
    ):
    radius -= jitter_pixel
    x, y = point_jitter(x, y, jitter_pixel)
    return mouse.get_random_point_in_circle_with_normal_distribution(
        x, y, radius, mu, sigma, range_x)


def get_random_point_in_rectangle(
        x: int,
        y: int,
        radius_x: int,
        radius_y: int,
        jitter_pixel: int = 1,
        mu: float = utils.MU,
        sigma: float = 1.2,
        range_x: int = utils.NORMAL_DISTRIBUTION_RANGE
    ):
    radius_x -= jitter_pixel
    radius_y -= jitter_pixel
    x, y = point_jitter(x, y, jitter_pixel)
    return mouse.get_random_point_in_rectangle_with_normal_distribution(
        x, y, radius_x, radius_y, mu, sigma, range_x)


def test_get_random_point_in_circle():
    x_: list[int] = []
    y_: list[int] = []
    for _ in range(5000):
        x, y = get_random_point_in_circle(0, 0, 100)
        x_.append(x)
        y_.append(y)

    # print(x_, y_)
    # pyplot.scatter(x_, y_, alpha=0.6, s=1)
    # pyplot.show()


def test_get_random_point_in_rectangle():
    x_: list[int] = []
    y_: list[int] = []
    for _ in range(5000):
        x, y = get_random_point_in_rectangle(0, 0, 100, 100)
        x_.append(x)
        y_.append(y)

    # print(x_, y_)
    # pyplot.scatter(x_, y_, alpha=0.6, s=1)
    # pyplot.show()


def get_distance(x1: float, y1: float, x2: float, y2: float) -> int:
    return round(math.sqrt((x1-x2)**2 + (y1-y2)**2))


def duration_left_to_right(distance: float):
    if 200 < distance:
        return distance / 800
    elif 100 < distance <= 200:
        return distance / 600
    elif distance <= 100:
        return distance / 200

    return 0


def duration_right_to_left(distance: float):
    if 200 < distance:
        return distance / 800
    elif 100 < distance <= 200:
        return distance / 600
    elif distance <= 100:
        return distance / 200

    return 0


def duration_up_and_down(distance: float):
    if 200 < distance:
        return distance / 800
    elif 100 < distance <= 200:
        return distance / 600
    elif distance <= 100:
        return distance / 200

    return 0


def move_to(x: int, y: int):
    # duration=pyautogui.MINIMUM_DURATION):
    # if duration < pyautogui.MINIMUM_DURATION:
    #     raise KanError('duration too short')
    current_x, current_y = pyautogui.position()
    if (current_x < x
            and (-1 < (y-current_y)/(x-current_x) < 1)):
        duration_function = duration_left_to_right
    elif (current_x > x
            and (-1 < (y-current_y)/(x-current_x) < 1)):
        duration_function = duration_right_to_left
    else:
        duration_function = duration_up_and_down

    duration = duration_function(get_distance(current_x, current_y, x, y))
    if duration <= 0.125:
        duration = 0.125
    duration = duration * (random.random() * 0.4 + 0.8)
    if duration < pyautogui.MINIMUM_DURATION:
        raise KanError('Duration too short')
    tween_function_table = [
        pyautogui.easeInQuad,
        pyautogui.easeInQuad,
        pyautogui.easeInQuad,
        pyautogui.easeOutQuad,
        pyautogui.easeOutQuad,
        pyautogui.easeOutQuad,
        pyautogui.easeInOutQuad,
        pyautogui.easeInOutQuad,
        pyautogui.easeInOutQuad,
        pyautogui.easeInOutQuad,
        pyautogui.easeInOutQuad
    ]
    tween_function = random.choice(tween_function_table)
    debug('before move: ({}, {})'.format(*pyautogui.position()))
    pyautogui.moveTo(x, y, duration=duration, tween=tween_function)
    debug('after move: ({}, {})'.format(*pyautogui.position()))


def click():
    debug('click here: ({}, {})'.format(*pyautogui.position()))
    pyautogui.click()


CLICK_TIMES = [1] * 60 + [2] * 30 + [3] * 10


def random_click_in_3():
    click_times = random.choice(CLICK_TIMES)
    if click_times == 1:
        pyautogui.click()
    elif click_times == 2:
        pyautogui.click(clicks=2, interval=(random.random() + 0.1))
        return
    time.sleep(0.5 + random.random())
    pyautogui.click()


def is_dot_in_rectangle(x: int, y: int, rect_x: int, rect_y: int, rect_radius_x: int, rect_radius_y: int):
    return ((rect_x - rect_radius_x <= x <= rect_x + rect_radius_x)
            and (rect_y - rect_radius_y <= y <= rect_y + rect_radius_y))


def is_dot_in_area(x: int, y: int, area: Area):
    if area.shape == Shape.rectangle:
        return is_dot_in_rectangle(
            x, y, area.x, area.y, area.radius_x, area.radius_y)
    else:
        raise NotImplementedError


def test_move_to():
    move_to(1200, 500)


def test_click():
    click()
    click()


def test():
    time.sleep(1)
    test_move_to()
    # test_get_random_point_in_rectangle()
    # test_click()


if __name__ == '__main__':
    test()

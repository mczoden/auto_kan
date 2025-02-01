"""Human play"""
import time
import random
# from matplotlib import pyplot
from typing import Iterable

import pyautogui

# import mouse
from utils import KanError
import human_mouse
import game_gui
from game_gui import Area, DotRgbChecker, Shape
# from game_gui import game_gui
from expedition_data import expedition_data as e_data

DEBUG_SKIP_WAIT = False
DEBUG_SKIP_CONFIRM = DEBUG_SKIP_WAIT
# DEBUG_SKIP_MOVE = DEBUG_SKIP_WAIT
DEBUG_SKIP_MOVE = False
DEBUG_DRAW_PYPLOT = False

position = 'start_to_test'
expedition_started = False
small_x: list[int] = []
small_y: list[int] = []
large_x: list[int] = []
large_y: list[int] = []


def debug(message: str):
    print('[{} Human Play] {}'.format(
        time.strftime("%m-%d %H:%M:%S", time.localtime()),
        message))


def short_sleep():
    if not DEBUG_SKIP_WAIT:
        time.sleep(1 + random.random() * 5)


def position_in_game() -> tuple[int, int]:
    x, y = pyautogui.position()
    x -= game_gui.offset_x
    y -= game_gui.offset_y
    return x, y


def is_mouse_in_area(area: Area):
    x, y = position_in_game()
    return human_mouse.is_dot_in_area(x, y, area)


def move_to_button(button: Area):
    if DEBUG_SKIP_MOVE:
        return
    x, y = 0, 0
    if button.shape == Shape.circle:
        x, y = human_mouse.get_random_point_in_circle(
            button.x, button.y, button.radius
        )
    elif button.shape == Shape.rectangle:
        x, y = human_mouse.get_random_point_in_rectangle(
            button.x, button.y, button.radius_x, button.radius_y
        )
    human_mouse.move_to(x + game_gui.offset_x, y + game_gui.offset_y)


def random_mouse_move(random_range: int = 40):
    if random_range <= 0 or random.random() > 0.4:
        return

    x, y = position_in_game()
    random_range = min([
        random_range,
        x,
        y,
        game_gui.window_area.x * 2 - x,
        game_gui.window_area.y * 2 - y,
    ])
    if random_range < 0:
        raise KanError('Random range < 0')

    if random_range == 0:
        return

    button = Area(Shape.circle, x, y, radius=random_range)
    move_to_button(button)


def confirm_areas(areas: Iterable[DotRgbChecker]):
    for area in areas:
        current_color = pyautogui.pixel(
            area.x + game_gui.offset_x,
            area.y + game_gui.offset_y)

        return area.ok(*current_color)


def is_at_port():
    return confirm_areas(game_gui.port_confirm_areas)


def is_at_sortie_main():
    return confirm_areas(game_gui.sortie_main_confirm_areas)


def is_at_expedition_in_sortie():
    return confirm_areas(game_gui.expedition_in_sortie_confirm_areas)


def is_at_supply():
    return confirm_areas(game_gui.supply_main_confirm_areas)


def wait_confirm_areas(
        areas: Iterable[DotRgbChecker],
        interval: float = 0.5,
        step: float = 0.5,
        timeout: float = float('inf')
    ):
    if DEBUG_SKIP_WAIT:
        return True
    total_wait_time = 0
    if timeout < 0:
        timeout = 0
    while True:
        if confirm_areas(areas):
            return True

        time.sleep(interval)
        interval += step
        total_wait_time += interval
        if total_wait_time >= timeout:
            return False


def wait_not_confirm_areas(
        areas: Iterable[DotRgbChecker],
        interval: float = 0.5,
        step: float = 0.5
    ):
    if DEBUG_SKIP_WAIT:
        return True
    while True:
        if not confirm_areas(areas):
            break
        if not DEBUG_SKIP_WAIT:
            time.sleep(interval)
            interval += step


def back_to_port_from_upper_left():
    global position
    if is_at_port():
        return
    button = game_gui.port_area

    condition = True
    while condition:
        move_to_button(button)
        time.sleep(random.random() * 0.2 + 0.2)
        human_mouse.click()
        time.sleep(1.5)
        if wait_confirm_areas(game_gui.port_confirm_areas, timeout=20):
            condition = False

    position = 'port'


def test_back_to_port_from_upper_left():
    back_to_port_from_upper_left()


def sortie_from_port():
    global position
    if is_at_sortie_main():
        return
    button = game_gui.sortie_in_port_area
    move_to_button(button)
    if not DEBUG_SKIP_WAIT:
        time.sleep(random.random() * 0.3 + 0.2)
    human_mouse.click()
    wait_confirm_areas(game_gui.sortie_main_confirm_areas)
    position = 'sortie'


def test_sortie_from_port():
    sortie_from_port()


def expedition_from_sortie():
    global position
    if is_at_expedition_in_sortie():
        return
    button = game_gui.expedition_in_sortie_area
    move_to_button(button)
    if not DEBUG_SKIP_WAIT:
        time.sleep(random.random() * 0.3 + 0.2)
    human_mouse.click()
    wait_confirm_areas(game_gui.expedition_in_sortie_confirm_areas)
    position = 'expedition_map1'


def test_expedition_from_sortie():
    expedition_from_sortie()


def select_center_x_from_bottom():
    raise NotImplementedError


def select_expedition_map_bottom_label(e: dict[str, int]):
    expedition_button = game_gui.map_areas_in_expedition[e['map']]
    move_to_button(expedition_button)
    if not DEBUG_SKIP_WAIT:
        time.sleep(random.random() * 0.2 + 0.2)
    human_mouse.click()
    global position
    position = 'expedition_map{}'.format(e['map'])
    if not DEBUG_SKIP_WAIT:
        time.sleep(random.random() * 0.5 + 0.5)


def get_expedition_virtual_button(e: dict[str, int]):
    global position
    # expedition bar in 80% scale is not symmetry in vertical
    # use base + height algorithm instead of center + radius
    center_y = (game_gui.first_expedition_base_y
                + (e['index'] - 1) * game_gui.expedition_height
                + game_gui.expedition_height // 2 - 1)
    radius_y = game_gui.expedition_height // 2 - 1
    # to make up the lost 1 pixel in bottom
    # make 1 pixel down overall, with 50% probability
    if random.choice([False, True]):
        center_y += 1

    if not position.startswith('expedition'):
        raise KanError('Not in expedition page')

    if position == 'expedition_map1':
        if e['map'] != 1:
            select_expedition_map_bottom_label(e)
    else:
        if position[-1] != str(e['map']):
            select_expedition_map_bottom_label(e)

    if random.randint(0, 100) < \
            game_gui.human_select_expedition_all_range_probability:
        # Low probability that user move to any place in expedition bar
        center_x = game_gui.expedition_center_x
        radius_x = game_gui.expedition_radius_x
        return Area(Shape.rectangle, center_x, center_y, radius_x, radius_y)

    # User always move up directly from bottom map label, with a little
    # horizontal displacement
    if is_mouse_in_area(game_gui.bottom_map_select_area):
        bottom_map_label_center_x = \
            game_gui.map_areas_in_expedition[e['map']].x
            # game_gui['map{}_in_expedition'.format(e['map'])]['x']
        radius_x = game_gui.human_select_expedition_from_bottom_radius_x
        center_x = bottom_map_label_center_x
        if center_x - radius_x < game_gui.expedition_left_x:
            center_x = game_gui.expedition_left_x + radius_x + 1

        return Area(Shape.rectangle, center_x, center_y, radius_x, radius_y)

    # User always move mouse from current position, with a little
    # horizontal displacement
    radius_x = game_gui.human_select_expedition_from_current_radius_x
    # Ensure that current_x +- radius_x not out of edge
    current_x, _ = position_in_game()
    center_x = current_x
    if current_x - radius_x < game_gui.expedition_left_x:
        center_x = game_gui.expedition_left_x + radius_x + 1
    elif current_x + radius_x > game_gui.expedition_right_x:
        center_x = game_gui.expedition_right_x - radius_x - 1

    return Area(Shape.rectangle, center_x, center_y, radius_x, radius_y)


def select_expedition(e_no: str):
    e = e_data[e_no]
    global position
    global small_x, small_y, large_x, large_y
    move_to_button(get_expedition_virtual_button(e))
    time.sleep(random.random() * 0.1 + 0.5)
    human_mouse.click()


def get_current_expedition_fleet():
    fleet = 0
    for i in range(2, 5):
        areas_to_check = \
            game_gui.expedition_fleets_is_selected_confirm_areas[i]
        if confirm_areas(areas_to_check):
            fleet = i
            break

    if fleet == 0:
        raise KanError('Fleet not found')

    return fleet


def wait_expedition_leave():
    global expedition_started
    if not expedition_started:
        raise KanError('expedition not started, call do_expedition firstly')

    wait_not_confirm_areas(game_gui.start_expedition_confirm_areas)
    # double confirm that expedition left
    wait_confirm_areas(game_gui.no_expedition_is_leaving_confirm_areas)
    time.sleep(0.5 + random.random())
    wait_confirm_areas(game_gui.no_expedition_is_leaving_confirm_areas)
    time.sleep(0.5 + random.random())


def do_expedition(fleet: int):
    move_to_button(game_gui.confirm_expedition_area)
    time.sleep(random.random() * 0.1 + 0.5)
    human_mouse.click()
    time.sleep(random.random() * 0.1 + 0.5)

    if fleet != get_current_expedition_fleet():
        time.sleep(random.random() * 0.1 + 0.2)
        move_to_button(game_gui.select_expedition_fleet_areas[fleet])
        time.sleep(random.random() * 0.1 + 0.2)
        human_mouse.click()

    current_x, current_y = position_in_game()
    if not human_mouse.is_dot_in_area(
            current_x, current_y, game_gui.start_expedition_area):
        move_to_button(game_gui.start_expedition_area)

    time.sleep(random.random() * 0.1 + 0.5)
    # pyautogui.confirm('click here')
    human_mouse.click()
    # FIXME: sleep is dirty solution
    debug('after click start')
    time.sleep(2)
    debug('after sleep 2 second')
    global expedition_started
    if expedition_started:
        raise KanError('expedition started already')
    expedition_started = True
    wait_expedition_leave()
    expedition_started = False


def check_all_expedition():
    if not is_at_port():
        back_to_port_from_upper_left()

    debug('move to expedition area')
    move_to_button(game_gui.expedition_check_area)
    time.sleep(random.random() * 0.5 + 0.2)

    while confirm_areas(game_gui.expedition_flag_confirm_areas):
        debug('click check area')
        human_mouse.click()
        random_mouse_move()
        time.sleep(1)
        wait_confirm_areas(game_gui.expedition_result_confirm_areas)

        while not confirm_areas(game_gui.port_confirm_areas):
            random_mouse_move()
            human_mouse.click()
            time.sleep(random.random() * 0.5 + 0.2)


def test_check_all_expedition():
    check_all_expedition()


def select_and_do_expedition(e_no: str, fleet: int):
    select_expedition(e_no)
    time.sleep(random.random() * 0.1 + 0.5)
    do_expedition(fleet)


def select_and_do_expeditions(e_f: list[tuple[str, int]]):
    for e_no, fleet in e_f:
        debug('{} - fleet {}'.format(e_no, fleet))
        select_and_do_expedition(e_no, fleet)


def goto_supply_from_port():
    global position
    if is_at_supply():
        return
    if not is_at_port():
        back_to_port_from_upper_left()
        time.sleep(random.random() * 0.5 + 0.5)
    button = game_gui.supply_in_port_area
    move_to_button(button)
    if not DEBUG_SKIP_WAIT:
        time.sleep(random.random() * 0.2 + 0.2)
    human_mouse.click()

    if not DEBUG_SKIP_WAIT:
        time.sleep(0.5)
    debug('Wait enter supply main page')
    wait_confirm_areas(game_gui.supply_main_confirm_areas)
    position = 'supply'


def test_goto_supply_from_port():
    goto_supply_from_port()


def get_current_supply_fleet():
    if not is_at_supply():
        raise KanError('Not in supply')

    fleet = 0
    for i in range(1, 5):
        areas_to_check = \
            game_gui.supply_fleets_is_selected_confirm_areas[i]
            # game_gui['supply_fleet{}_is_selected_confirm_areas'.format(i)]
        if confirm_areas(areas_to_check):
            fleet = i
            break

    if fleet == 0:
        raise KanError('Fleet not found')

    return fleet


def test_get_current_supply_fleet():
    while True:
        try:
            print(get_current_supply_fleet())
        except KanError as e:
            print(e)
        time.sleep(1)


def select_fleet_to_supply(fleet: int):
    # move_to_button(game_gui['fleet{}_in_supply'.format(fleet)])
    move_to_button(game_gui.fleet_in_supply_areas[fleet])
    time.sleep(random.random() * 0.5 + 0.1)
    human_mouse.click()
    while fleet != get_current_supply_fleet():
        time.sleep(0.2)


def is_need_to_supply():
    return confirm_areas(game_gui.first_ship_need_to_supply_confirm_areas)


def supply(fleet: int):
    if fleet < 1 or fleet > 4:
        raise KanError('Invalid fleet number')
    if fleet != get_current_supply_fleet():
        select_fleet_to_supply(fleet)

    if not is_need_to_supply():
        return

    move_to_button(game_gui.supply_all_in_supply_area)
    time.sleep(random.random() * 0.5 + 0.2)
    # pyautogui.confirm('click here')
    human_mouse.click()
    wait_not_confirm_areas(game_gui.first_ship_need_to_supply_confirm_areas)
    time.sleep(random.random() + 0.5)


def test_supply():
    # supply(1)
    supply(2)
    time.sleep(2)
    supply(3)


def test_select_expedition():
    select_expedition('17')
    time.sleep(3)
    select_expedition('02')
    time.sleep(3)
    select_expedition('09')

    if not DEBUG_DRAW_PYPLOT:
        return
    # ax = fig.add_subplot(111)

    global small_x, small_y, large_x, large_y
    small_x += large_x
    small_y += large_y
    # ax.scatter(small_x, small_y, s=4, c='b', marker='s', label='small')
    # ax.scatter(large_x, large_y, s=4, c='r', marker='o', label='large')
    # pyplot.show()


def test():
    if not DEBUG_SKIP_WAIT:
        time.sleep(3)
    '''
    test_back_to_port_from_upper_left()
    if not DEBUG_SKIP_WAIT:
        time.sleep(random.random() * 0.5 + 0.2)
    test_sortie_from_port()
    if not DEBUG_SKIP_WAIT:
        time.sleep(random.random() * 0.5 + 0.2)
    test_expedition_from_sortie()
    if not DEBUG_SKIP_WAIT:
        time.sleep(random.random() * 0.5 + 0.2)
    # global position
    # position = 'expedition_map2'
    test_select_expedition()
    '''
    # test_goto_supply_from_port()
    # test_supply()
    #
    # test_check_all_expedition()
    # for i in range(100):
    #    time.sleep(1)
    #    random_mouse_move()

    # test_get_current_supply_fleet()
    '''
    while True:
        if is_at_port():
            print('Port')
        else:
            print('Not port')
        time.sleep(2)
    '''
    time.sleep(3)
    global position
    position = 'expedition_map1'
    while True:
        for i in range(1, 9):
            select_expedition('0' + str(i))
            time.sleep(random.random())


if __name__ == '__main__':
    test()

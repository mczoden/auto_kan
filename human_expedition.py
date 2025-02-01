"""Auto expedition core algorithm simulate human's behavior"""
# import threading
import time
import random

from utils import KanError
import expedition


DEBUG = False
NEVER_FORGET = False

if not DEBUG:
    CHECK_RESERVE_TIME = 5 * 60
    WAIT_TIME_BETWEEN_2_COMING_MISSIONS = 5 * 60
else:
    CHECK_RESERVE_TIME = 5
    WAIT_TIME_BETWEEN_2_COMING_MISSIONS = 5


class HumanExpedition(expedition.Expedition):
    def __init__(self, expedition_id: str, expedition_time: int, expedition_fleet: int):
        expedition.Expedition.__init__(self, expedition_id, expedition_time,
                                       expedition_fleet)


INIT_MISSION_LIST = [
    HumanExpedition('2', 18, 1),
    HumanExpedition('5', 54, 2),
    HumanExpedition('21', 84, 3)
]


class HumanExpeditionPool(expedition.ExpeditionPool):
    def __init__(self, check_reserve_time: int = CHECK_RESERVE_TIME):
        expedition.ExpeditionPool.__init__(self, check_reserve_time)


def debug(message: str):
    print('[{} Human Expedition] {}'.format(
        time.strftime("%m-%d %H:%M:%S", time.localtime()),
        message))


def probability_of_any_event_will_occur(probability_list: list[float]):
    for r in probability_list:
        if r > 1:
            print(probability_list)
            raise KanError('Rate larger than 1')

    tmp = 1
    for r in probability_list:
        tmp *= (1 - r)

    return 1 - tmp


def forget_to_check(expedition_pool: HumanExpeditionPool) -> bool:
    if NEVER_FORGET:
        return False
    complete_pool = expedition_pool.get_complete_pool()
    max_expedition_time = max([m.expedition_time for m in complete_pool])

    if not complete_pool:
        raise KanError('Empty complete pool')

    forget_probability_table: list[float] = [0, 0.1, 0.1, 0]
    forget_probability_based_on_expedition_number = \
        forget_probability_table[len(complete_pool)]
    if max_expedition_time <= 1800:
        forget_probability_based_on_max_expedition_time = 0.4
    elif 1800 < max_expedition_time <= 10800:
        forget_probability_based_on_max_expedition_time = 0.2
    else:
        forget_probability_based_on_max_expedition_time = 0.1

    forget_probability = probability_of_any_event_will_occur([
        forget_probability_based_on_max_expedition_time,
        forget_probability_based_on_expedition_number])

    is_forget = random.random() < forget_probability
    if is_forget:
        debug('Forget to check expedition')
        debug('Complete pool:\n\t{}'.format(
            '\n\t'.join([str(m) for m in complete_pool])))

    return is_forget


def random_sleep_forget_to_check(expedition_pool: HumanExpeditionPool):
    next_expedition_remaining_time = \
        expedition_pool.get_next_expedition_remaining_time()

    if next_expedition_remaining_time == float('inf'):
        return

    multiple_table = [0.5] * 95 + [1.5] * 5
    multiple = random.choice(multiple_table)
    if multiple == 0.5:
        time_to_sleep = random.randint(
            int(next_expedition_remaining_time * 0),
            int(next_expedition_remaining_time * 0.5))
    else:
        time_to_sleep = random.randint(
            int(next_expedition_remaining_time * 0.5),
            int(next_expedition_remaining_time * 1))
    debug('Random sleep to forget check expedition: {}s'.format(time_to_sleep))
    time.sleep(time_to_sleep)
    debug('Sleep complete')


def random_sleep_between_complete_and_check(expedition_pool: HumanExpeditionPool):
    # sleep time should not longer than CHECK_RESERVE_TIME
    sleep_time = (random.choice(range(10, 100)) / 100
                  * expedition_pool.check_reserve_time * 0.5)
    debug('Random sleep between complete and check: {} s'.format(sleep_time))
    time.sleep(sleep_time)
    debug('Sleep complete')


def main_control():
    """Main process"""
    human_expedition_pool = HumanExpeditionPool(check_reserve_time=5)

    for human_expedition in INIT_MISSION_LIST:
        human_expedition_pool.new_running_expedition(human_expedition)

    while True:
        if human_expedition_pool.is_expedition_almost_complete():
            debug('Expedition complete coming')
            human_expedition_pool.wait_to_check_expedition()

        if not human_expedition_pool.is_complete_expedition_empty():
            if forget_to_check(human_expedition_pool):
                random_sleep_forget_to_check(human_expedition_pool)
                continue
            random_sleep_between_complete_and_check(human_expedition_pool)
            human_expedition_pool.check_expedition()

        if not human_expedition_pool.is_ready_expedition_empty():
            human_expedition_pool.do_expedition()

        # print(human_expedition_pool)
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            # print(human_expedition_pool)
            break


if __name__ == '__main__':
    main_control()
